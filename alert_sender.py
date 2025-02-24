#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText

def send_alert(config, message):
    """Sends an alert email."""
    try:
        smtp_server = config.get("smtp_server")
        smtp_port = config.get("smtp_port", 587)
        smtp_user = config.get("smtp_user")
        smtp_password = config.get("smtp_password")
        alert_recipients = config.get("alert_recipients", [])

        if not all([smtp_server, smtp_user, smtp_password, alert_recipients]):
            print("Warning: SMTP configuration incomplete. Skipping alert.")
            return

        msg = MIMEText(message)
        msg["Subject"] = "Server Log Alert"
        msg["From"] = smtp_user
        msg["To"] = ", ".join(alert_recipients)

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Use TLS encryption
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, alert_recipients, msg.as_string())

        print("Alert email sent successfully.")

    except smtplib.SMTPAuthenticationError:
        print("Error: SMTP authentication failed. Check your username and password.")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
