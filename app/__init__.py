from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'
    
    # Import models
    from app.models.book import Book
                                    
    db.init_app(app)
    migrate.init_app(app, db)    
                                        
    # Register Blueprints 
    from .routes import books_bp
    app.register_blueprint(books_bp) 

    return app