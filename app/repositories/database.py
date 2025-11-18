from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os 
from dotenv import load_dotenv

# cargamos las variables de entorno
load_dotenv()

# accedemos a las variables de entorno
DB_USER = os.getenv("DATABASE_USER")
DB_PASS = os.getenv("DATABASE_PASSWORD")
DB_NAME = os.getenv("DATABASE_NAME")

# URL de conexion a SQLite
""" Agregar variables de entorno """
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@localhost:3306/{DB_NAME}"


# Crear motor de conexion a la base de datos
engine = create_engine(
    DATABASE_URL
)

# Crear una sesion para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para definir los modelos de las tablas
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
