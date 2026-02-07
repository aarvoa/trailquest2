from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

# Import Layers
from app.api.repository.repository import Repo
from app.api.services.services import Service
from app.api.controller.controller import Controller

# Register Routes
from app.routes import register_routes

# Initialize App
app = FastAPI(title="TrailQuest")

# Base Path
BASE_DIR = Path(__file__).resolve().parent

# Mount Static Files
# app/web/static -> /static
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "web" / "static")), name="static")

# Templates Configuration
templates = Jinja2Templates(directory=str(BASE_DIR / "web" / "templates"))

# Initialize Dependencies
# In a real app, 'db' would be a real database connection
db = [] 
repo = Repo(db)
service = Service(repo)
controller = Controller(service, templates)

register_routes(app, controller)
