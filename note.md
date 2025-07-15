# Furhter Notice
1. Logging per-request (HTTP request, error)
2. 🛠 Logger untuk request API (Flask route logging)
3. Migrasi model otomatis (Flask-Migrate)

4. Bacth sections:
    1. 🔁 Setup Flask-Migrate + Alembic
    2. 🐳 Integrasi ke Docker & Docker Compose
    3. 🔐 Deployment Gunicorn + Nginx

5. Middleware

# NOTE CODE:

## app/__init__.py
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    """
    Membuat instance Flask + load config + inisialisasi DB.
    """
    app = Flask(__name__)

    # Peta environment ke modul konfigurasi
    env = os.getenv("FLASK_ENV", "development").lower()
    config_map = {
        "development": "config.development.DevelopmentConfig",
        "staging": "config.staging.StagingConfig",
        "production": "config.production.ProductionConfig",
        "test": "config.test.TestConfig"
    }
    app.config.from_object(config_map[env])
    db.init_app(app)

    # Buat semua tabel dari model untuk semua engine (bukan hanya SQLite)
    with app.app_context():
        from . import models
        db.create_all()
        print("[INFO] All models initialized.")

    return app
```

```python
def create_app():
    app = Flask(__name__)
    env = os.getenv("FLASK_ENV", "development").lower()
    config_map = {
        "development": "config.development.DevelopmentConfig",
        "staging": "config.staging.StagingConfig",
        "production": "config.production.ProductionConfig",
        "test": "config.test.TestConfig"
    }
    app.config.from_object(config_map[env])
    db.init_app(app)

    with app.app_context():
        from . import models
        db.create_all()
    return app
```

## db_checker.py
```python
import socket

def is_postgresql_running(host='localhost', port=5432, timeout=2) -> bool:
    """
    Mengecek apakah PostgreSQL aktif di host:port.
    Mengembalikan True jika koneksi berhasil, False jika ditolak.
    """
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

```

## all fallback code
```python
import os
import socket
from contextlib import closing

from config.logger import setup_logger

logger = setup_logger()  # Inisialisasi logger


# --------------------------------------------------------------------------- #
# Utilitas kecil                                                              #
# --------------------------------------------------------------------------- #
def _tcp_ping(host: str, port: int, timeout: float = 2.0) -> bool:
    """Cek TCP connect ke host:port."""
    try:
        with closing(socket.create_connection((host, port), timeout=timeout)):
            return True
    except OSError:
        return False


def _build_sqlite_uri(db_dir_abs: str, db_name: str) -> str:
    """Pastikan folder & file SQLite, lalu kembalikan URI."""
    if not db_name:
        raise ValueError("DB_NAME must be set for SQLite fallback.")

    db_file_path = os.path.join(db_dir_abs, db_name)

    if os.path.exists(db_file_path):
        logger.info("SQLite DB already exists at %s", db_file_path)
    else:
        logger.info("SQLite DB will be created at %s", db_file_path)

    return f"sqlite:///{db_file_path}"


# --------------------------------------------------------------------------- #
# Resolver                                                                    #
# --------------------------------------------------------------------------- #
def resolve_database_uri(prefix: str) -> str:
    """Bangun URI dari env dan fallback ke SQLite bila server remote mati."""

    # --- Ambil variabel ENV ------------------------------------------------- #
    engine = os.getenv(f"{prefix}_DB_ENGINE")
    driver = os.getenv(f"{prefix}_DB_DRIVER", "").strip() or None
    username = os.getenv(f"{prefix}_DB_USERNAME", "").strip() or None
    password = os.getenv(f"{prefix}_DB_PASSWORD", "").strip() or None
    host = os.getenv(f"{prefix}_DB_HOST", "").strip() or None
    port = os.getenv(f"{prefix}_DB_PORT", "").strip() or None
    db_name = os.getenv(f"{prefix}_DB_NAME")
    db_path = os.getenv(f"{prefix}_DB_PATH", "storage")

    # --- Siapkan folder storage -------------------------------------------- #
    db_dir_abs = os.path.abspath(db_path)
    os.makedirs(db_dir_abs, exist_ok=True)

    # --- Jika engine SQLite langsung return -------------------------------- #
    if engine == "sqlite":
        return _build_sqlite_uri(db_dir_abs, db_name)

    # ----------------------------------------------------------------------- #
    # ENGINE selain SQLite: ping dulu                                          #
    # ----------------------------------------------------------------------- #
    port_int = int(port or 0) if port else None
    remote_ok = _tcp_ping(host or "localhost", port_int or 5432)

    if not remote_ok:
        # Fallback ke SQLite
        logger.warning(
            "Remote DB %s://%s:%s tidak dapat dihubungi ➜ fallback ke SQLite",
            engine,
            host,
            port,
        )
        return _build_sqlite_uri(db_dir_abs, f"{prefix.lower()}_fallback.db")

    # Jika ping sukses, bangun URI remote
    auth = f"{username}:{password}@" if username and password else ""
    driver_part = f"+{driver}" if driver else ""
    host_part = f"{host}:{port}" if host else ""

    return f"{engine}{driver_part}://{auth}{host_part}/{db_name}"


# --------------------------------------------------------------------------- #
# Helper publik dipakai BaseConfig                                            #
# --------------------------------------------------------------------------- #
def get_database_uri() -> str:
    env = (os.getenv("FLASK_ENV") or "development").lower()

    prefix_map = {
        "development": "DEV",
        "staging": "STAGING",
        "production": "PROD",
        "test": "TEST",
    }
    prefix = prefix_map.get(env)
    if not prefix:
        raise ValueError(f"Unsupported FLASK_ENV: {env}")

    return resolve_database_uri(prefix)
```