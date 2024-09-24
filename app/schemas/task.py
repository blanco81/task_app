from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class TaskCreate(BaseModel):
    task_name: str
    description: Optional[str] = None
    user_id: UUID

class TaskUpdate(BaseModel):
    task_name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class TaskResponse(BaseModel):
    id: UUID
    task_name: str
    description: Optional[str]
    status: str
    ip_address: Optional[str]
    country: Optional[str]
    weather: Optional[str]
    user_id: UUID

    class Config:
        orm_mode = True
