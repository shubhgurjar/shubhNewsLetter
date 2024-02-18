from flask import Flask, render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect
from dev.models.db_model import db

def create_app(config=None):
    app = Flask(__name__)
    
    if config:
        app.config.from_object(config)
    
    # Initialize CSRF protection
    csrf = CSRFProtect(app)

    # Initialize extensions
    db.init_app(app)

    # Create tables
    with app.app_context():
        db.create_all()
    
    # Register blueprints, set up routes, etc.
    # app.add_url_rule(...)

    from dev.main.routes import main
    from dev.users.routes import users

    app.register_blueprint(main)
    app.register_blueprint(users)

    # app.app_context().push()
   
    
    return app
