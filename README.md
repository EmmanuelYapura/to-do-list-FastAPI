# 📋 To‑Do List – FastAPI

Una API REST básica desarrollada con **FastAPI** para gestionar una lista de tareas (*tasks*), con operaciones CRUD: crear, leer, actualizar y eliminar tareas.

---

## 🧱 Tecnologías

### 🔙 Backend
- **FastAPI** 
- **SQLAlchemy** 
- **Pydantic** 
- **Uvicorn** 
- **SQLite** 
- **Jinja2**  

### 🎨 Frontend
- **HTML5** 
- **CSS3** 

---

## 🚀 Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/EmmanuelYapura/to-do-list-FastAPI.git "nombre_carpeta"
   cd "nombre_carpeta"
   ```

2. Crea un entorno virtual e instala dependencias:

   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows

   pip install -r requirements.txt
   ```

3. Levantar el servidor:

   ```bash
   - uvicorn app.main:app --reload
   ```

4. Ingresar al puerto:

   ```bash
   http://127.0.0.1:8000
   ```

---

## ▶️ Documentacion automatica

Accediendo a:

- `http://127.0.0.1:8000/docs` – Swagger UI interactivo  
- `http://127.0.0.1:8000/redoc` – Documentación con ReDoc

---

## 📡 Endpoints Basicos

- `GET /task` – Lista todas las tareas  
- `GET /task/{id}` – Obtiene una tarea por ID  
- `GET /edit_task/{id}` – Permite editar una tarea por ID
- `POST /task` – Crea una nueva tarea  
- `POST /task/{id}/update` – Actualiza una tarea existente  
- `POST /task/{id}/delete` – Elimina una tarea existente

---

## 🧪 Ejemplos de uso

### Crear una tarea

```http
POST /task
Content-Type: application/json

{
  "nombre": "ejemplo de tarea",
  "completa": false,
  "importante": false
}
```

### Respuesta

```json
{
  "id": 1,
  "nombre": "ejemplo de tarea",
  "completa": false,
  "importante": false
}
```

---

## ⚙️ Estructura del proyecto

```
app/
├── controllers/               # Controladores: definen los endpoints y lógica de enrutamiento
├── repositories/              # Capa de acceso a datos
│   ├── models/                # Modelos ORM y conexión a la base de datos
│   │   ├── __init__.py
│   │   ├── database.py        # Configuración de la base de datos (SQLite)
│   │   └── tasks_repository.py # Funciones CRUD sobre tareas
├── schema/                    # Esquemas Pydantic: validación de entrada/salida
├── services/                  # Lógica de negocio 
├── static/                    # Archivos estáticos 
├── templates/                 # Plantillas HTML para Jinja2
├── main.py                    # Punto de entrada principal de la app FastAPI
task.db                        # Base de datos SQLite (si se está usando SQLite localmente)
requirements.txt               # Dependencias del proyecto
```

---

## 🤝 Contribuciones

¡Bienvenido! Podés contribuir generando issues, haciendo PRs o sugiriendo mejoras.  
En tu contribución, por favor detallá qué hiciste, chequeá el formato de código, y mantené las dependencias actualizadas.

---

## 👤 Autor

Desarrollado por **Emmanuel Yapura** –