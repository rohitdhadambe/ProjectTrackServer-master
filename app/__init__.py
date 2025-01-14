from flask import Flask
from app.extensions import db
from app.config import Config
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Enable CORS for the specified origin
    CORS(app, resources={r"/*": {"origins": ["http://localhost:5173"]}},
         supports_credentials=True,
         allow_headers=["Content-Type", "Authorization"])

    app.config.from_object(Config)

    # Initialize the database
    db.init_app(app)

    # Import models to register them with SQLAlchemy
    from app.models import Admin

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Register blueprints for routes
    from app.routes import register_blueprints
    register_blueprints(app)

    return app
