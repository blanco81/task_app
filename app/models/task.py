from sqlalchemy import Column, Integer, String, ForeignKey
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import Text
from sqlalchemy.orm import relationship
from app.db.base import Base

class Task(Base):
    __tablename__ = "task"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    task_name = Column(String, index=True)
    description = Column(Text, nullable=True)
    status = Column(String, default="pending", nullable=False)
    ip_address = Column(String, nullable=True)
    country = Column(String, nullable=True)
    weather = Column(String, nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'), nullable=False)
    user = relationship("User", back_populates="tasks")
    
    