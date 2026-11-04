from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Booking
from ..services.availability import is_slot_free, list_free_slots
from ..services.notifications import send_confirmation

router = APIRouter()


class BookingRequest(BaseModel):
    practitioner_id: int
    patient_name: str
    patient_email: EmailStr
    patient_phone: str | None = None
    reason: str | None = None
    start_time: datetime


@router.get("/slots/{practitioner_id}")
def get_slots(practitioner_id: int, day: str, db: Session = Depends(get_db)):
    return list_free_slots(db, practitioner_id, datetime.fromisoformat(day).date())


@router.post("/")
def create_booking(req: BookingRequest, db: Session = Depends(get_db)):
    if not is_slot_free(db, req.practitioner_id, req.start_time):
        raise HTTPException(status_code=409, detail="Slot already taken")
    booking = Booking(**req.model_dump())
    db.add(booking)
    db.commit()
    db.refresh(booking)
    send_confirmation(booking)
    return {"id": booking.id, "status": "confirmed"}


@router.post("/{booking_id}/cancel")
def cancel_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.get(Booking, booking_id)
    if not booking:
        raise HTTPException(status_code=404)
    booking.cancelled = True
    db.commit()
    return {"id": booking.id, "status": "cancelled"}
