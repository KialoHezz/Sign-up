# from distutils.debug import DEBUG
import os

class config:
    SECRET_KEY=os.environ.get('SECRET_KEY')

class Devconfig(config):
    DEBUG = True

class ProdConfig(config):
    pass

config_options = {
    'development': Devconfig,
    'production': ProdConfig
}