from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

import os

db = SQLAlchemy()

def create_app():
    # Ambil environment yang sudah diset oleh run.py
    env = os.getenv("FLASK_ENV").lower()

    # Load file .env sesuai FLASK_ENV
    env_file = f".env.{env}"

    if os.path.exists(env_file):
        load_dotenv(env_file)

    else:
        print(f"⚠️ File {env_file} tidak ditemukan. Menggunakan konfigurasi default.")


    # 0. core flask configuration
    core = Flask(__name__, 
                static_url_path = '/', 
                static_folder = 'static', 
                template_folder = 'templates'
                )
    
    # 2. __init__ configuration sections
    from config import register_config

    config = register_config()
    core.config.from_object(config)

    # 1. __init__ routes sections
    from app.routes import register_routes

    register_routes(core)

    # 3. __init__ models sections
    from app.models import db
    db.init_app(core)

    # 4. pembuatan table 
    with core.app_context():
        from app import models # mengambil semua data yang ada pada model pada var __all__
        db.create_all()
        print("[INFO] All models initialized.")

    return core