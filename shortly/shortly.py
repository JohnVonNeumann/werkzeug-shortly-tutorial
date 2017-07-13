import os
import redis
import urlparse
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader

class Shortly(object):
    """Create an object that will act as an implementation of WSGI
    """

    def __init__(self, config):
        self.redis = redis.Redis(config['redis_host'], config['redis_port'])

    def dispatch_request(self, request):
        return Response('Hello, World!')

    """ :param:`~environ` autopopulates via the host, this was talked about
    in pep333 as a key item of WSGI, it changes as the application server
    delivers indivdual resources, like pages, and favicons
    """
    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        print(request)
        response = self.dispatch_request(request)
        print(response)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def create_app(redis_host='localhost', redis_port=6379, with_static=True):
    """Create an app object and pass in some keyword args
    """
    app = Shortly({
        'redis_host':        redis_host,
        'redis_port':        redis_port
    })
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static': os.path.join(os.path.dirname(__file__), 'static')
        })
    return app


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)


