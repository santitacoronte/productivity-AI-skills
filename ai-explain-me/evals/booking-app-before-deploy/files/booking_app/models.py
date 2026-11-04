from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from .database import Base


class Practitioner(Base):
    __tablename__ = "practitioners"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialty = Column(String)
    bookings = relationship("Booking", back_populates="practitioner", cascade="all, delete")


class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    practitioner_id = Column(Integer, ForeignKey("practitioners.id"), nullable=False)
    patient_name = Column(String, nullable=False)
    patient_email = Column(String, nullable=False)
    patient_phone = Column(String)
    reason = Column(String)  # free text, may contain medical details
    start_time = Column(DateTime, nullable=False)
    cancelled = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    practitioner = relationship("Practitioner", back_populates="bookings")
