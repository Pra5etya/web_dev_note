from config.base import BaseConfig
import os

class ProductionConfig(BaseConfig):
    DEBUG = False
    ENV = "production"
    SQLALCHEMY_DATABASE_URI = BaseConfig.SQLALCHEMY_DATABASE_URI
