from apscheduler.schedulers.background import BackgroundScheduler
from config.backup import backup_database
import os

def start_backup_scheduler():
    """
    Menjadwalkan backup otomatis:
    - Tiap 6 jam
    - Tiap hari jam 01:00
    - Tiap minggu hari Senin jam 02:00
    """
    scheduler = BackgroundScheduler()

    env = os.getenv("FLASK_ENV").lower()
    prefix = env.upper()

    # ✅ Backup tiap 6 jam
    scheduler.add_job(
        func = lambda: backup_database(prefix),
        trigger = 'interval',
        hours = 6,
        id = 'six_hour_backup',
        replace_existing = True
    )

    # ✅ Backup harian jam 01:00
    scheduler.add_job(
        func = lambda: backup_database(prefix),
        trigger = 'cron',
        hour = 1,
        minute = 0,
        id = 'daily_backup',
        replace_existing = True
    )

    # ✅ Backup mingguan setiap Senin jam 02:00
    scheduler.add_job(
        func = lambda: backup_database(prefix),
        trigger = 'cron',
        day_of_week = 'mon',
        hour = 2,
        minute = 0,
        id = 'weekly_backup',
        replace_existing = True
    )

    scheduler.start()
    print("[INFO] Scheduler aktif:")
    print("- Setiap 6 jam")
    print("- Setiap hari pukul 01:00")
    print("- Setiap Senin pukul 02:00")
