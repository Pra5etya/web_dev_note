import os, logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

def setup_logger(log_name="log"):
    """
    Menyiapkan logger khusus untuk informasi database.
    Setiap hari akan dibuat file log baru dengan format: logs/db_info_YYYY-MM-DD.log
    """

    os.makedirs("logs", exist_ok = True)

    today_str = datetime.now().strftime("%Y-%m-%d")
    log_file = f"logs/{log_name}_{today_str}.log"

    logger = logging.getLogger(log_name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # Ganti ke TimedRotatingFileHandler (rotasi harian)
        handler = TimedRotatingFileHandler(
            filename = log_file,
            when = "midnight",           # Rotasi tiap tengah malam
            interval = 1,                # Setiap 1 hari
            backupCount = 30,             # Simpan 7 hari terakhir
            encoding = 'utf-8',
            utc = False                  # Rotasi berdasarkan waktu lokal
        )

        formatter = logging.Formatter("[%(asctime)s] \t %(levelname)s: \t %(message)s")
        handler.setFormatter(formatter)

        # Gunakan suffix agar nama file hasil rotasi konsisten
        handler.suffix = "%Y-%m-%d"

        logger.addHandler(handler)

    return logger
