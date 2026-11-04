import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./bookings.db")

# Email settings for confirmations
SMTP_HOST = "smtp.sendgrid.net"
SMTP_PORT = 587
SMTP_USER = "apikey"
SMTP_PASSWORD = "SG.FAKE-TEST-KEY-not-a-real-secret"  # TODO move to env
FROM_EMAIL = "bookings@clinic-example.com"

OPENING_HOUR = 9
CLOSING_HOUR = 17
SLOT_MINUTES = 30
TIMEZONE = "UTC"
