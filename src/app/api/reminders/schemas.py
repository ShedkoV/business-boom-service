from pydantic import BaseModel
from datetime import datetime


class BaseReminder(BaseModel):

    user_phone: str
    reminder_text: str
    reminder_time: datetime


class ReminderRequest(BaseReminder):
    """..."""


class ReminderResponse(BaseReminder):
    id: int

    class Config:
        from_attributes = True
