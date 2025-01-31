from sqlalchemy import select

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.reminders.schemas import ReminderRequest, ReminderResponse
from app.storages.database import get_async_session
from app.storages.models.reminders import Reminder

default_session = Depends(get_async_session)


class RemindersService:
    def __init__(self, session: AsyncSession = default_session) -> None:
        self._session = session

    async def create_reminder(self, request: ReminderRequest) -> ReminderResponse:
        db_reminder = Reminder(**request.dict())
        self._session.add(db_reminder)
        try:
            await self._session.commit()
            await self._session.refresh(db_reminder)
        except Exception as e:
            raise e
        return ReminderResponse.from_orm(db_reminder)

    async def get_reminders(self):
        result = await self._session.execute(select(Reminder))
        return result.scalars().all()
