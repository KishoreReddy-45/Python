import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "alerts@company.com"
    msg["To"] = to_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("alerts@company.com", "app-password")
        server.send_message(msg)

if __name__ == "__main__":
    send_email("ETL Failure", "The pipeline failed at step X", "data.team@company.com")
