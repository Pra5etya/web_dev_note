import os
from config.utils import get_database_uri
from config.logger import setup_db_logger

class BaseConfig:
    """
    Base configuration class untuk semua environment Flask (dev, prod, etc.).
    """
    SQLALCHEMY_DATABASE_URI = get_database_uri()  # Di-resolve dari .env
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = os.getenv("DEBUG")

    # Setup logger ketika konfigurasi di-load
    setup_db_logger()
