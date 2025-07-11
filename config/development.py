from config.base import BaseConfig
import os

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ENV = "development"
    SQLALCHEMY_DATABASE_URI = BaseConfig.SQLALCHEMY_DATABASE_URI
