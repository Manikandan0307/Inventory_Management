
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class addproduct(FlaskForm):
    productid = StringField('Product ID', validators=[DataRequired()])
    prodname = StringField('Product Name', validators=[DataRequired()])
    prodqty = IntegerField('Quantity', validators=[NumberRange(min=5, max=1000000), DataRequired()])
    prodsubmit = SubmitField('Save Changes')

class editproduct(FlaskForm):
    editid = StringField('Product ID', validators=[DataRequired()])
    editname = StringField('Product Name', validators=[DataRequired()])
    editqty = IntegerField('Quantity', validators=[NumberRange(min=5, max=1000000), DataRequired()])
    editsubmit = SubmitField('Save Changes')

class addlocation(FlaskForm):
    locid = StringField('Location ID', validators=[DataRequired()])
    locname = StringField('Location Name', validators=[DataRequired()])
    locsubmit = SubmitField('Save Changes')

class editlocation(FlaskForm):
    editlocid = StringField('Location ID', validators=[DataRequired()])
    editlocname = StringField('Location Name', validators=[DataRequired()])
    editlocsubmit = SubmitField('Save Changes')

class moveproduct(FlaskForm):
    movementid = StringField('Movement ID', validators=[DataRequired()])
    mprodname = SelectField('Product Name')
    src = SelectField('Source')
    destination = SelectField('Destination')
    mprodqty = IntegerField('Quantity', validators=[NumberRange(min=5, max=1000000), DataRequired()])
    movesubmit = SubmitField('Move')
