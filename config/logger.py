import os
import logging
from logging.handlers import RotatingFileHandler

def setup_db_logger(log_name = "db_info", log_file = "logs/db_info.log"):
    """
    Menyiapkan logger khusus untuk informasi database.
    Log akan disimpan ke 'logs/db_info.log', rotasi otomatis jika besar log > 1MB.
    """
    os.makedirs(os.path.dirname(log_file), exist_ok = True)  # Buat folder logs jika belum ada

    logger = logging.getLogger(log_name)
    logger.setLevel(logging.INFO)  # Hanya log INFO ke atas (INFO, WARNING, ERROR)

    if not logger.handlers:
        handler = RotatingFileHandler(log_file, maxBytes = 1_000_000, backupCount = 3)
        formatter = logging.Formatter("[%(asctime)s] \t %(levelname)s: \t %(message)s")
        
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
