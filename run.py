from app import create_app
from config.backup import backup_database
from dotenv import load_dotenv

import os, sys, time

load_dotenv(".env.default")                                 # Muat konfigurasi dari .env.default terlebih dahulu
local_cfg = os.getenv("LOCAL_CONFIG")                       # Ambil nilai LOCAL_CONFIG, dari .env.default

env_secret_path = os.path.join(local_cfg, ".env.secret")    # Buat path manual ke .env.secret
load_dotenv(env_secret_path, override = True)               # Lalu override dengan konfigurasi rahasia jika ada

valid_envs = set(os.getenv("VALID_ENVS").split(","))        # Ambil environment yang valid

# default value
def_env = os.getenv("DEFAULT_ENV")
def_host = os.getenv("DEFAULT_HOST")
def_port = int(os.getenv("DEFAULT_PORT"))

# Override dari CLI
if len(sys.argv) > 1 and sys.argv[1] in valid_envs:
    def_env = sys.argv[1]

os.environ["FLASK_ENV"] = def_env


# Backup database sesuai environment dan engine
prefix = def_env.upper()
backup_database(prefix)


# Inisialisasi aplikasi
app = create_app()

if __name__ == "__main__":
    print(f'Start Application: {os.environ["FLASK_ENV"]} \n')     # Hanya untuk testing, jika sudah hapus kembali !!!
    time.sleep(3)                                                 # Hanya untuk testing, jika sudah hapus kembali !!!

    app.run(debug = (def_env != "production"), 
            host = def_host, 
            port = def_port)
