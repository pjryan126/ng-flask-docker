from flask import Flask
import jinja2

from config import config


# Subclass Flask application class to replace global Jinja loader.
class App(Flask):
    def __init__(self):
        Flask.__init__(self, __name__)
        self.jinja_loader = jinja2.ChoiceLoader([
            self.jinja_loader,
            jinja2.PrefixLoader({}, delimiter='.')
        ])

    def create_global_jinja_loader(self):
        return self.jinja_loader

    def register_blueprint(self, bp, **options):
        Flask.register_blueprint(self, bp, **options)
        self.jinja_loader.loaders[1].mapping[bp.name] = bp.jinja_loader


def register_blueprints(app):

    from .blueprints.main import main
    app.register_blueprint(main)

    return app


def register_extensions(app):

    from flask_cors import CORS
    cors = CORS()
    cors.init_app(app)

    return app


def create_app(config_name):
    app = Flask(__name__, static_folder='static')

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    register_extensions(app)
    register_blueprints(app)

    return app
