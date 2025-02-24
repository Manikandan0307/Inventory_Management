# Inventory Management Web Application

## 📌 Project Overview
This is a **Flask-based Inventory Management Web Application** that allows users to manage products, locations, and track inventory movement. The system enables CRUD operations on products and locations, and provides an overview of inventory balances at different locations.

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Backend:** Flask (Python), SQLAlchemy
- **Database:** MySQL


## ✨ Features
- **Products Management**: Add, edit, delete products
- **Locations Management**: Add, edit, delete locations
- **Product Movements**: Track product transfers between locations
- **Balance Report**: View inventory balance at different locations


## 📥 Installation Guide
### 1️⃣ Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- MySQL Database
- Flask and required dependencies








### 5️⃣ Configure Database
- Create a MySQL database and update `config.py` with your credentials:
```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/inventory_db'
```
- Initialize the database:
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### 6️⃣ Run the Application
```bash
flask run
```
- Open **http://127.0.0.1:5000/** in your browser.

## 📸 Screenshots
### Dashboard Page
![Dashboard Page](./flaskinventory/static/./screenshots/dashboard.jpg)



### Product Page
![Product page](./flaskinventory/static/screenshots/products.png)


### Location Page

![Location page](./flaskinventory/static/screenshots/./location.jpg)

### Transfer Page

![Transfer page](./flaskinventory/static/screenshots/Transfers.jpg)


### Balance Page
![balance page](./flaskinventory/static/screenshots/balance.jpg)










## 🚀 Future Enhancements
- User authentication & role-based access
- API integration for third-party services
- Export reports in PDF/Excel
- Deploying on a cloud platform

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

## 📜 License
This project is licensed under the MIT License.



