from config.base import BaseConfig
import os

class StagingConfig(BaseConfig):
    DEBUG = True
    ENV = "staging"
    SQLALCHEMY_DATABASE_URI = BaseConfig.SQLALCHEMY_DATABASE_URI