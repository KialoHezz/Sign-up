from config import config_options
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
# from flask_mail import Mail
# from app import db
from flask_sqlalchemy import SQLAlchemy
# from flask_uploads import IMAGES, UploadSet, configure_uploads


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.signin'
# init dabatabase
db = SQLAlchemy()
# photos = UploadSet('photos', IMAGES)
bootstrap = Bootstrap()
# mail = Mail()


def create_app(config_name):
    app = Flask(__name__)

    # app configuration
    app.config.from_object(config_options[config_name])



    # configure UploadSet
    # configure_uploads(app,photos)


    # init flask extensions for
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    # mail.init_app(app)
    
    # register our blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #url_prefix argument that will add a prefix to all the routes registered with that blueprint.
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authentication')


    return app

