from flask import Flask, render_template, request, jsonify
from dev.models.db_model import db

def create_app(config=None):
    app = Flask(__name__)
    
    if config:
        app.config.from_object(config)
    
    # Initialize extensions
    db.init_app(app)

    # Create tables
    with app.app_context():
        db.create_all()
    
    # Register blueprints, set up routes, etc.
    # app.register_blueprint(...)
    # app.add_url_rule(...)

    from dev.main import home

    app.register_blueprint(home.main)

    # app.app_context().push()
   
    
    return app
