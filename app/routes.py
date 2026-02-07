from fastapi import FastAPI
from app.api.controller.controller import Controller

def register_routes(app: FastAPI, controller: Controller):
    app.add_api_route("/", controller.read_root, methods=["GET"])
    app.add_api_route("/game", controller.play_page, methods=["GET"])
    app.add_api_route("/game/start", controller.start_game, methods=["POST"])
    
    # Game Details
    app.add_api_route("/game/{game_id}", controller.get_game_details, methods=["GET"])
    
    # Game Steps
    app.add_api_route("/game/{game_id}/step/{step_id}/content", controller.get_step_content, methods=["GET"])
    app.add_api_route("/game/{game_id}/step/{step_id}/fact", controller.get_step_fact, methods=["GET"])