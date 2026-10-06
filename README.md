# 📈 FinApp - Investment Portfolio & Treasury Bonds Management

<div align="center">

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-black?style=for-the-badge&logo=flask&logoColor=white)
![Azure SQL](https://img.shields.io/badge/Azure_SQL-Cloud_Database-0089D6?style=for-the-badge&logo=microsoftazure&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap_5-UI-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

**A secure, cloud-connected web application designed to manage, track, and analyze retail treasury bond portfolios and financial assets.**

</div>

---

## 🚀 About the Project

**FinApp** is a robust web application built to solve real-world personal finance tracking challenges—specifically tailored for Polish retail treasury bonds and investment portfolios using a lot-based tracking model. 

Recently migrated from a local relational database to **Microsoft Azure SQL Cloud**, this project demonstrates modern **Data Engineering practices**, secure connection string management via ODBC, and robust Object-Relational Mapping (ORM).

---

## 🛠️ Tech Stack & Architecture

* **Back-end:** Python, Flask, Flask-Login, Flask-SQLAlchemy
* **Cloud Database:** Microsoft Azure SQL Database (Cloud PaaS)
* **Data Processing & Analysis:** Pandas, NumPy
* **Database Driver:** ODBC Driver 18 for SQL Server (`pyodbc`)
* **Front-end:** Bootstrap 5, Jinja2, Chart.js for dynamic financial visualizations
* **Environment Security:** `python-dotenv` for secure credential management

---

## ⚙️ Key Features

* **Cloud-Native Data Storage:** Fully migrated to Azure SQL with secure TLS/SSL encryption (`Encrypt=yes`).
* **Lot-Based Portfolio Tracking:** Precise tracking of bond purchases, interest capitalization, and maturity dates.
* **Data Aggregation & Analytics:** Uses `Pandas` to process transaction history and calculate portfolio performance metrics.
* **Secure Authentication:** Password hashing and session management via Flask-Login.
* **Interactive Visualizations:** Dynamic charts rendered with `Chart.js` reflecting portfolio asset distribution.

---

## 📂 Project Structure

```text
aplikacja-portfela-inwestycyjnego/
│
├── app/
│   ├── blueprints/         # Modular blueprints (Auth, Dashboard, Portfolio)
│   ├── models.py           # SQLAlchemy database models (Users, Bonds, Transactions)
│   ├── static/             # CSS, JavaScript and images
│   ├── templates/          # HTML templates (Jinja2)
│   └── __init__.py         # App factory and Azure DB initialization
│
├── .env                    # Local environment variables (git-ignored)
├── config.py               # Configuration class with Azure ODBC connection string
├── requirements.txt        # Project dependencies
└── run.py                  # Entry point for running the application
