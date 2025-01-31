from pydantic import BaseModel
from datetime import date


class BaseReminder(BaseModel):

    user_phone: str
    reminder_text: str
    reminder_time: date


class ReminderRequest(BaseReminder):
    """..."""


class ReminderResponse(BaseReminder):
    id: int

    class Config:
        from_attributes = True
