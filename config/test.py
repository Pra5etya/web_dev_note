from config.base import BaseConfig
import os

class TestConfig(BaseConfig):
    DEBUG = False
    ENV = "test"
    SQLALCHEMY_DATABASE_URI = BaseConfig.SQLALCHEMY_DATABASE_URI
