import smtplib
from email.message import EmailMessage

from ..config import FROM_EMAIL, SMTP_HOST, SMTP_PASSWORD, SMTP_PORT, SMTP_USER


def send_confirmation(booking):
    msg = EmailMessage()
    msg["Subject"] = "Your appointment is confirmed"
    msg["From"] = FROM_EMAIL
    msg["To"] = booking.patient_email
    msg.set_content(
        f"Hello {booking.patient_name},\n\n"
        f"Your appointment is booked for {booking.start_time:%Y-%m-%d %H:%M}.\n"
        f"Reason: {booking.reason}\n\n"
        "To cancel, reply to this email."
    )
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as s:
        s.starttls()
        s.login(SMTP_USER, SMTP_PASSWORD)
        s.send_message(msg)
