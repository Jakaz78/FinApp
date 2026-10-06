import os
from dotenv import load_dotenv
import urllib

load_dotenv()


class Config:
    # Flask
    SECRET_KEY = os.getenv("SECRET_KEY")
    JSON_AS_ASCII = False

    # Database - Azure SQL Server (ODBC)
    server = os.getenv("AZURE_SERVER")
    database = os.getenv("AZURE_DB")
    username = os.getenv("AZURE_USER")
    password = os.getenv("AZURE_PASSWORD")
    driver = "{ODBC Driver 18 for SQL Server}"

    odbc_str = (
        f"DRIVER={driver};"
        f"SERVER={server};"
        f"PORT=1433;"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
        f"Encrypt=yes;"
        f"TrustServerCertificate=no;"
        f"Connection Timeout=30;"
    )

    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(odbc_str)}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # Poprawione dzielenie plików
    SQLALCHEMY_ECHO = True  # Dla deweloperki

    # App
    THEMES = ["Dark", "Light"]
    LANGUAGES = ["Polski", "English", "Deutsch"]
    DEFAULT_SETTINGS = {"theme": "Dark", "language": "Polski"}