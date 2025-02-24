from flask import current_app
from . import db
from datetime import datetime

class Location(db.Model):
    location_id = db.Column(db.String(20), primary_key=True)
    loc_name = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"Location('{self.location_id}', '{self.loc_name}')"

class Product(db.Model):
    product_id = db.Column(db.String(20), primary_key=True)
    prod_name = db.Column(db.String(20), unique=True, nullable=False)
    prod_qty = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Product('{self.product_id}', '{self.prod_name}', '{self.prod_qty}')"

class ProductMovement(db.Model):
    movement_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    from_location = db.Column(db.String(20), db.ForeignKey('location.location_id'), nullable=False)
    to_location = db.Column(db.String(20), db.ForeignKey('location.location_id'), nullable=False)
    product_id = db.Column(db.String(20), db.ForeignKey('product.product_id'), nullable=False)
    qty = db.Column(db.Integer, nullable=False)

class Balance(db.Model):
    bid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.String(50), nullable=False)
    product = db.Column(db.String(50), nullable=False) 
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Balance('{self.bid}', '{self.product}', '{self.location}', '{self.quantity}')"