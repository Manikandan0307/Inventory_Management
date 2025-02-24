# run.py

from flaskinventory import app, db

# Ensure this is inside the application context
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
