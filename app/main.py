from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

# Initialize App
app = FastAPI(title="TrailQuest")

# Base Path
BASE_DIR = Path(__file__).resolve().parent

# Mount Static Files
# app/web/static -> /static
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "web" / "static")), name="static")

# Templates Configuration
templates = Jinja2Templates(directory=str(BASE_DIR / "web" / "templates"))

# Basic Route (Recursive/Temporary pending full router setup)
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# Play Page
@app.get("/play")
async def play_page(request: Request):
    return templates.TemplateResponse("play.html", {"request": request})

# Game Start (Stub)
@app.post("/play/start")
async def start_game(request: Request):
    form_data = await request.form()
    # TODO: Validate game_id, access_code, team_name
    return {"message": "Game starting...", "data": form_data}
