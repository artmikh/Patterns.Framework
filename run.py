from wsgiref.simple_server import make_server
from main import Application
from urls import routes
from front_controller import fronts


class Run:

    def __init__(self, app, port):
        self.app = app
        application = app

        with make_server('', port, application) as httpd:
            print(f"Serving on port {port}...")
            httpd.serve_forever()


if __name__ == '__main__':
    start = Run(Application(routes, fronts), 8000)
