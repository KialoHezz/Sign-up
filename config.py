import os

class config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    # connecting to gmail
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # connecting postgres db
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hezzykialo:admin12345@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'


class Devconfig(config):
    DEBUG = True

class ProdConfig(config):
    pass

config_options = {
    'development': Devconfig,
    'production': ProdConfig
}