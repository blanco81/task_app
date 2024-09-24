from fastapi import FastAPI
from app.api import auth, tasks
from app.db.session import engine
from app.db.base import Base
import uvicorn

app = FastAPI(title="Tasks API with OAuth2")

app.include_router(auth.router, tags=["auth"])
app.include_router(tasks.router, tags=["tasks"])

# Crear las tablas en la base de datos
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, timeout_keep_alive=3600)