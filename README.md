# Inventory Management Web Application

## 📌 Project Overview
This is a **Flask-based Inventory Management Web Application** that allows users to manage products, locations, and track inventory movement. The system enables CRUD operations on products and locations, and provides an overview of inventory balances at different locations.

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Backend:** Flask (Python), SQLAlchemy
- **Database:** MySQL
- **Hosting:** Local development (Can be deployed on Heroku, AWS, or any cloud platform)

## ✨ Features
- **Products Management**: Add, edit, delete products
- **Locations Management**: Add, edit, delete locations
- **Product Movements**: Track product transfers between locations
- **Balance Report**: View inventory balance at different locations
- **Pagination & Filtering**: Easily browse through records

## 📥 Installation Guide
### 1️⃣ Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- MySQL Database
- Flask and required dependencies

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/inventory-management.git
cd inventory-management
```

### 3️⃣ Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

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
![Dashboard](static/screenshots/./dashboard.jpg)
### Product page
![Product](static/screenshots/./product.jpg)
### Location page
![location](static/screenshots/./location.jpg)
### Transfers page
![Transfers](static/screenshots/./transfers.jpg)
### Balance page
![Balance](static/screenshots/./balance.jpg)




## 🚀 Future Enhancements
- User authentication & role-based access
- API integration for third-party services
- Export reports in PDF/Excel
- Deploying on a cloud platform

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

## 📜 License
This project is licensed under the MIT License.



