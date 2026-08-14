import smtplib
from email.message import EmailMessage
from config.config import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD, REPORT_RECIPIENT

def send_report(file_path):
    msg = EmailMessage()
    msg["Subject"] = "NEPSE Daily Market Report"
    msg["From"] = EMAIL_USER
    msg["To"] = REPORT_RECIPIENT
    msg.set_content("Today's NEPSE market report is attached.")

    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="text",
            subtype="html",
            filename=file_path.name,
        )

    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_USER, EMAIL_PASSWORD)
        smtp.send_message(msg)
