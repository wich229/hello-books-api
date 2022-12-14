from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)

    from .routes import book_dp
    app.register_blueprint(book_dp) 

    return app