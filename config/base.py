import os
from config.data import get_database_uri

class BaseConfig:
    """
    Base configuration class untuk semua environment Flask (dev, prod, etc.).
    """
    SQLALCHEMY_DATABASE_URI = get_database_uri()  # Di-resolve dari .env
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = os.getenv("DEBUG")