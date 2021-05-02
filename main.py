from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
from views import *
from front_controller import *
from urls import *


class Application:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        setup_testing_defaults(environ)
        print('work')
        path = environ['PATH_INFO']
        # Если в пути есть '/' в конце, то убираем его
        if path[-1] == '/':
            path = path[:-1]
        if path in self.routes:
            view = self.routes[path]
        else:
            view = Not_found_404()
        request = {}
        # front controller
        for front in self.fronts:
            front(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return body


application = Application(routes, fronts)

with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
