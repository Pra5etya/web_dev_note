import os


"""
File ini hanya menyiapkan konfigurasi database, tanpa inisialisasi DB.
"""


sqlite_dir = os.getenv('SQLITE_DIR', 'instance')
sqlite_name = os.getenv('SQLITE_NAME', 'sample.db')

def load_env():
    db_dir_abs = os.path.abspath(sqlite_dir)

    if not os.path.exists(db_dir_abs): 
        os.makedirs(db_dir_abs)
        print(f"[INFO] Created database directory at {db_dir_abs}")

    db_file_path = os.path.join(db_dir_abs, sqlite_name)

    # Cek apakah DB file sudah ada
    if os.path.exists(db_file_path):
        print(f"[INFO] Database already exists at {db_file_path}. Skipping creation.\n")
        
    else:
        print(f"[INFO] Database does not exist yet at {db_file_path}. It will be created when models are initialized.\n")

    return db_file_path

def configure_app_database(app):
    db_path = load_env()

    secret_key = os.getenv('SECRET_KEY')
    if not secret_key:
        raise RuntimeError("SECRET_KEY is required but not set in environment")
    app.config['SECRET_KEY'] = secret_key

    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    print(f"[INFO] Database configured with URI: sqlite:///{db_path}")
