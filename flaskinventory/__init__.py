
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Mrperfect@123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Mani@localhost/flaskinventory'
db = SQLAlchemy(app)

from flaskinventory import routes

with app.app_context():
    db.create_all()
    db.session.commit()
