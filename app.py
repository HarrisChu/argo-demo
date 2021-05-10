# -*- coding: utf-8 -*-
import sys
import logging
from flask import Flask

from argo_demo.controller import blueprint


def create_app(config_object="argo_demo.settings"):
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split(".")[0])
    # app.config.from_object(config_object)
    register_blueprints(app)
    configure_logger(app)
    return app


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(blueprint)
    pass


def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
