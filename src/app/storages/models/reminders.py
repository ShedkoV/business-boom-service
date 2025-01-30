from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.declarative import declarative_base


Base: DeclarativeMeta = declarative_base()


class Reminder(Base):  # type: ignore[valid-type, misc]
    """Table views in database."""

    __tablename__ = 'reminders'

    id = Column(Integer, primary_key=True)
    user_phone = Column(String)
    reminder_text = Column(String)
    reminder_time = Column(DateTime)
