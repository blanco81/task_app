from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.crud.task import create_task, get_all_tasks, get_task_by_id, update_task, delete_task
from app.db.session import get_db
from app.core.security import get_current_user
from app.utils.ip_info import get_ip_info
from app.utils.weather import get_weather_info
from app.models.user import User
from datetime import datetime
from uuid import UUID
import requests

router = APIRouter()

@router.post("/tasks", response_model=TaskResponse)
async def create_new_task(
    task: TaskCreate,
    db: AsyncSession = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    ip_address = requests.get("https://api.ipify.org").text
    latitude, longitude = get_ip_info(ip_address)
    if latitude is None or longitude is None:
        raise HTTPException(status_code=400, detail="Could not retrieve location from IP")
    
    weather_info = get_weather_info(latitude, longitude)
    country = weather_info.get("country")
    weather = weather_info.get("weather")
    
        
    # Crear la tarea
    new_task = await create_task(db, task, ip_address, country, weather, current_user.id)
    return new_task

@router.get("/tasks", response_model=list[TaskResponse])
async def read_tasks(
    db: AsyncSession = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    tasks = await get_all_tasks(db)
    return tasks

@router.get("/tasks/{task_id}", response_model=TaskResponse)
async def read_task(
    task_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    task = await get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_existing_task(
    task_id: UUID,
    task_update: TaskUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    updated_task = await update_task(db, task_id, task_update)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@router.delete("/tasks/{task_id}")
async def delete_existing_task(
    task_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    deleted_task = await delete_task(db, task_id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted successfully"}
