from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from uuid import UUID

async def create_task(db: AsyncSession, task: TaskCreate, ip: str, country: str, weather: str, user_id: UUID):
    new_task = Task(
        task_name=task.task_name,
        description=task.description,
        ip_address=ip,
        country=country,
        weather=weather,
        user_id=user_id
    )
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task

async def get_all_tasks(db: AsyncSession):
    result = await db.execute(select(Task))
    return result.scalars().all()

async def get_task_by_id(db: AsyncSession, task_id: UUID):
    result = await db.execute(select(Task).filter(Task.id == task_id))
    return result.scalars().first()

async def update_task(db: AsyncSession, task_id: UUID, task_update: TaskUpdate):
    task = await get_task_by_id(db, task_id)
    if not task:
        return None
    if task_update.task_name is not None:
        task.task_name = task_update.task_name
    if task_update.description is not None:
        task.description = task_update.description
    if task_update.status is not None:
        task.status = task_update.status
    await db.commit()
    await db.refresh(task)
    return task

async def delete_task(db: AsyncSession, task_id: int):
    task = await get_task_by_id(db, task_id)
    if not task:
        return None
    await db.delete(task)
    await db.commit()
    return task
