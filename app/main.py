from fastapi import FastAPI
from app.controllers.tasks_controllers import router
from app.repositories.database import Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(router=router)
