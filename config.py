import os

class config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    # connecting to gmail
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # connecting postgres db
    UPLOADED_PHOTOS_DEST ='app/static/photos'


class Devconfig(config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
    DEBUG = True

class ProdConfig(config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    

config_options = {
    'development': Devconfig,
    'production': ProdConfig
}