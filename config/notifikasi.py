from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.logger import setup_db_logger

import os, smtplib, requests


logger = setup_db_logger()

# ========================
# 📧 EMAIL NOTIFICATION
# ========================
def send_email_notification(subject, message):
    try:
        smtp_server = os.getenv("EMAIL_SMTP_SERVER")
        smtp_port = int(os.getenv("EMAIL_SMTP_PORT", 587))
        sender_email = os.getenv("EMAIL_SENDER")
        sender_password = os.getenv("EMAIL_PASSWORD")
        recipient_email = os.getenv("EMAIL_RECIPIENT")

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject

        msg.attach(MIMEText(message, "plain"))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        logger.info("📧 Email notification sent.")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")

# ========================
# 📱 TELEGRAM NOTIFICATION
# ========================
def send_telegram_notification(message):
    try:
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")

        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": chat_id, "text": message}

        response = requests.post(url, data=data)
        if response.status_code == 200:
            logger.info("📱 Telegram notification sent.")
        else:
            logger.error(f"Failed to send Telegram message: {response.text}")
    except Exception as e:
        logger.error(f"Error sending Telegram message: {e}")

# ========================
# 💬 WHATSAPP NOTIFICATION (via Twilio)
# ========================
'''
def send_whatsapp_notification(message):
    try:
        from twilio.rest import Client

        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        from_whatsapp = os.getenv("TWILIO_WHATSAPP_FROM")  # e.g., 'whatsapp:+14155238886'
        to_whatsapp = os.getenv("TWILIO_WHATSAPP_TO")      # e.g., 'whatsapp:+628123456789'

        client = Client(account_sid, auth_token)
        client.messages.create(body=message, from_=from_whatsapp, to=to_whatsapp)

        logger.info("💬 WhatsApp notification sent.")
    except Exception as e:
        logger.error(f"Failed to send WhatsApp message: {e}")
'''

# ========================
# 🔔 MASTER FUNCTION
# ========================
def send_all_notifications(subject, message):
    send_email_notification(subject, message)
    send_telegram_notification(message)

    # send_whatsapp_notification(message)
