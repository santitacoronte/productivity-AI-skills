from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Booking, Practitioner

router = APIRouter()


@router.get("/bookings")
def all_bookings(db: Session = Depends(get_db)):
    # Returns every booking with patient details for the front desk screen
    return db.query(Booking).all()


@router.post("/practitioners")
def add_practitioner(name: str, specialty: str = "", db: Session = Depends(get_db)):
    p = Practitioner(name=name, specialty=specialty)
    db.add(p)
    db.commit()
    return {"id": p.id}


@router.delete("/practitioners/{practitioner_id}")
def remove_practitioner(practitioner_id: int, db: Session = Depends(get_db)):
    p = db.get(Practitioner, practitioner_id)
    if p:
        db.delete(p)
        db.commit()
    return {"deleted": practitioner_id}
