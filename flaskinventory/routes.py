from flask import render_template, url_for, redirect, flash, request
from flaskinventory import app, db
from flaskinventory.forms import addproduct, addlocation, moveproduct, editproduct, editlocation
from flaskinventory.models import Location, Product, ProductMovement, Balance
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import uuid

@app.route("/")
@app.route("/overview")
def overview():
    balance = Balance.query.all()
    if not balance:
        flash('Add products, locations, and make transfers to view balance.', 'info')
    return render_template('overview.html', balance=balance)

@app.route("/Product", methods=['GET', 'POST'])
def product():
    form = addproduct()
    eform = editproduct()
    details = Product.query.all()
    exists = bool(Product.query.all())
    if not exists and request.method == 'GET':
        flash('Add products to view', 'info')
    elif eform.validate_on_submit() and request.method == 'POST':
        p_id = request.form.get("productid", "")
        pname = request.form.get("productname", "")
        prod = Product.query.filter_by(product_id=p_id).first()
        prod.prod_name = eform.editname.data
        prod.prod_qty = eform.editqty.data
        Balance.query.filter_by(product=pname).update(dict(product=eform.editname.data))
        ProductMovement.query.filter_by(product_id=pname).update(dict(product_id=eform.editname.data))
        try:
            db.session.commit()
            flash('Your product has been updated!', 'success')
        except IntegrityError:
            db.session.rollback()
            flash('This product already exists', 'danger')
    elif form.validate_on_submit():
        product = Product(product_id=form.productid.data, prod_name=form.prodname.data, prod_qty=form.prodqty.data)
        db.session.add(product)
        try:
            db.session.commit()
            flash(f'Your product {form.prodname.data} has been added!', 'success')
        except IntegrityError:
            db.session.rollback()
            flash('This product already exists', 'danger')
    return render_template('product.html', title='Products', eform=eform, form=form, details=details)

@app.route("/Location", methods=['GET', 'POST'])
def loc():
    form = addlocation()
    lform = editlocation()
    details = Location.query.all()
    exists = bool(Location.query.all())
    if not exists and request.method == 'GET':
        flash('Add locations to view', 'info')
    if lform.validate_on_submit() and request.method == 'POST':
        p_id = request.form.get("locid", "")
        locname = request.form.get("locname", "")
        loc = Location.query.filter_by(location_id=p_id).first()
        loc.loc_name = lform.editlocname.data
        Balance.query.filter_by(location=locname).update(dict(location=lform.editlocname.data))
        ProductMovement.query.filter_by(from_location=locname).update(dict(from_location=lform.editlocname.data))
        ProductMovement.query.filter_by(to_location=locname).update(dict(to_location=lform.editlocname.data))
        try:
            db.session.commit()
            flash('Your location has been updated!', 'success')
        except IntegrityError:
            db.session.rollback()
            flash('This location already exists', 'danger')
    elif form.validate_on_submit():
        loc = Location(location_id=form.locid.data, loc_name=form.locname.data)
        db.session.add(loc)
        try:
            db.session.commit()
            flash(f'Your location {form.locname.data} has been added!', 'success')
        except IntegrityError:
            db.session.rollback()
            flash('This location already exists', 'danger')
    return render_template('loc.html', title='Locations', lform=lform, form=form, details=details)

@app.route("/Transfers", methods=['GET', 'POST'])
def move():
    form = moveproduct()
    details = ProductMovement.query.all()
    pdetails = Product.query.all()
    exists = bool(ProductMovement.query.all())
    if not exists and request.method == 'GET':
        flash('Transfer products to view', 'info')
    prod_choices = Product.query.with_entities(Product.product_id, Product.prod_name).all()
    loc_choices = Location.query.with_entities(Location.location_id, Location.loc_name).all()
    prod_list_names = [(prod[0], prod[1]) for prod in prod_choices]
    src_list_names = [(loc[0], loc[1]) for loc in loc_choices]
    dest_list_names = [(loc[0], loc[1]) for loc in loc_choices]
    form.mprodname.choices = prod_list_names
    form.src.choices = src_list_names
    form.destination.choices = dest_list_names

    if form.validate_on_submit() and request.method == 'POST':
        timestamp = datetime.now()
        boolbeans = check(form.src.data, form.destination.data, form.mprodname.data, form.mprodqty.data)
        if boolbeans == False:
            flash('Retry with lower quantity than source location', 'danger')
        elif boolbeans == 'same':
            flash('Source and destination cannot be the same.', 'danger')
        elif boolbeans == 'no prod':
            flash('Not enough products in this location. Please add products', 'danger')
        else:
            mov = ProductMovement(
                timestamp=timestamp,
                from_location=form.src.data,
                to_location=form.destination.data,
                product_id=form.mprodname.data,
                qty=form.mprodqty.data
            )
            product = Product.query.filter_by(product_id=form.mprodname.data).first()
            if product.prod_qty < form.mprodqty.data:
                flash(f'Cannot move more than available quantity of {product.prod_name}.', 'danger')
            else:
                product.prod_qty -= form.mprodqty.data
                db.session.add(mov)
                db.session.commit()
                flash('Your activity has been added!', 'success')
        return redirect(url_for('move'))
    return render_template('move.html', title='Transfers', form=form, details=details)

@app.route("/delete/<string:type>/<string:p_id>", methods=['GET', 'POST'])
def delete(type, p_id):
    try:
        if type == 'product':
            ProductMovement.query.filter_by(product_id=p_id).delete()
            Product.query.filter_by(product_id=p_id).delete()
            flash('Product deleted successfully!', 'success')
        elif type == 'location':
            ProductMovement.query.filter((ProductMovement.from_location == p_id) | 
                                          (ProductMovement.to_location == p_id)).delete()
            Location.query.filter_by(location_id=p_id).delete()
            flash('Location deleted successfully!', 'success')
        else:
            flash('Error deleting item.', 'danger')
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        flash('Unable to delete item due to foreign key constraints.', 'danger')
    return redirect(url_for('overview'))

from sqlalchemy import text  # Import text module

@app.route('/balance', methods=['GET'])
def show_balance():
    # Explicitly declare the SQL statement as text
    balance_query = text("""
        INSERT INTO balance (location, product, quantity)
        SELECT l.loc_name, p.prod_name, p.prod_qty
        FROM location l, product p
        ON DUPLICATE KEY UPDATE quantity = p.prod_qty;
    """)

    db.session.execute(balance_query)  # Execute the query
    db.session.commit()  # Commit changes to the database

    balance_data = Balance.query.all()  # Fetch updated balance data
    return render_template('balance.html', title='Balance', balance=balance_data)

def check(frm, to, name, qty):
    if frm == to:
        return 'same'
    elif frm == 'Warehouse' and to != 'Warehouse':
        prodq = Product.query.filter_by(prod_name=name).first()
        if prodq and prodq.prod_qty >= int(qty):
            return True
        else:
            return 'no prod'
    if frm == 'Warehouse' or to == 'Warehouse':
        return True
    try:
        qty = int(qty)
    except ValueError:
        return 'invalid qty'
    return True
