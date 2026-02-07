from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

class Controller:
    def __init__(self, service, templates: Jinja2Templates):
        self.service = service
        self.templates = templates
        
    async def read_root(self, request: Request):
        return self.templates.TemplateResponse("home.html", {"request": request})

    async def play_page(self, request: Request):
        return self.templates.TemplateResponse("play.html", {"request": request})

    async def start_game(self, request: Request):
        form_data = await request.form()
        game_id = form_data.get("game_id", "UNKNOWN")
        team_name = form_data.get("team_name", "Adventurers")
        
        # In a real app, verify game_id exists here.
        # For now, redirect to the game description page.
        # Encode team_name properly in a real app.
        return RedirectResponse(url=f"/game/{game_id}?team_name={team_name}", status_code=303)

    async def get_game_details(self, request: Request, game_id: str, team_name: str = "Adventurers"):
        # Mock Data - In reality this would come from the Service/Repo
        # Fetch current step for this team/game
        current_step_id = 1
        
        context = {
            "request": request,
            "game_title": "The Mystery of the Hidden Valley",
            "game_description": "Embark on a thrilling quest through the ancient forests and treacherous peaks of the Hidden Valley. Solve riddles, find clues, and uncover the secrets of a lost civilization before time runs out!",
            "game_id": game_id,
            "team_name": team_name,
            "current_step_id": current_step_id
        }
        return self.templates.TemplateResponse("game_description.html", context)
        
    async def get_step_content(self, request: Request, game_id: str, step_id: int):
        # Mock Data for Step 1
        # Target: Eiffel Tower (just as an example coordinate) -> 48.8584, 2.2945
        # User will probably mock this in dev tools
        target_lat = 52.41169332458407
        target_lng = 13.413143329387628
        description = "Go to the Iron Lady of Paris. Stand beneath her arches."
        
        context = {
            "request": request,
            "game_id": game_id,
            "step_id": step_id,
            "target_lat": target_lat,
            "target_lng": target_lng,
            "description": description
        }
        return self.templates.TemplateResponse("content_page.html", context)

    async def get_step_fact(self, request: Request, game_id: str, step_id: int):
        return {"message": f"You reached step {step_id}! Fact page coming soon."}