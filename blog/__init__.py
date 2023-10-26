from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretjutsu'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://giannis:1234@localhost:5433/blog'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)

    from .models import User, Blog, Category
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth/')
  
    return app