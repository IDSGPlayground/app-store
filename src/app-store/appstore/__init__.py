from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import DBSession
import os

here = os.path.dirname(os.path.abspath(__file__))

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', os.path.join(here, 'static'))
    # config.add_static_view('static/css', 'static:css', cache_max_age=3600)
    config.add_route('browse', '/')
    config.scan()
    return config.make_wsgi_app()
