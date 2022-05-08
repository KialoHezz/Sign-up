from distutils.debug import DEBUG


class config:
    pass

class Devconfig(config):
    DEBUG = True

class ProdConfig(config):
    pass

config_options = {
    'development': Devconfig,
    'production': ProdConfig
}