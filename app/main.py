from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.tasks_controllers import router
from app.controllers.tasks_api import router_api
from app.repositories.database import Base, engine

from fastapi.staticfiles import StaticFiles

app = FastAPI(title = "To Do List API", version="1.0.0")

# agregando CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","http://localhost:3000"], #modificar origin proximamente
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.mount('/static', StaticFiles(directory='app/static'), 'static')
Base.metadata.create_all(bind=engine)
app.include_router(router=router)
app.include_router(router=router_api)

@app.get("/")
def root():
    return{"message": "API funcionando correctamente con CORS activo"}