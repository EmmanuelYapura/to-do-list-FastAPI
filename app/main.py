from fastapi import FastAPI
from app.controllers.tasks_controllers import router
from app.repositories.database import Base, engine

from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount('/static', StaticFiles(directory='app/static'), 'static')
Base.metadata.create_all(bind=engine)
app.include_router(router=router)
