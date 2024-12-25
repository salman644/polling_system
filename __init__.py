from flask import Flask
from app.routes.poll_routes import poll_routes
from app.routes.vote_routes import vote_routes

def create_app():
    app = Flask(__name__)

    # Register blueprints for routes
    app.register_blueprint(poll_routes)
    app.register_blueprint(vote_routes)

    return app

