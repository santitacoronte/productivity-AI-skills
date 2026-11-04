from datetime import date, datetime, timedelta

from sqlalchemy.orm import Session

from ..config import CLOSING_HOUR, OPENING_HOUR, SLOT_MINUTES
from ..models import Booking


def _all_slots(day: date):
    current = datetime(day.year, day.month, day.day, OPENING_HOUR)
    end = datetime(day.year, day.month, day.day, CLOSING_HOUR)
    while current < end:
        yield current
        current += timedelta(minutes=SLOT_MINUTES)


def is_slot_free(db: Session, practitioner_id: int, start: datetime) -> bool:
    existing = (
        db.query(Booking)
        .filter(Booking.practitioner_id == practitioner_id, Booking.start_time == start)
        .first()
    )
    return existing is None


def list_free_slots(db: Session, practitioner_id: int, day: date):
    return [s.isoformat() for s in _all_slots(day) if is_slot_free(db, practitioner_id, s)]
