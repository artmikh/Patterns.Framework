from wsgiref.simple_server import make_server
from main import Application
from urls import routes
from front_controller import fronts


application = Application(routes, fronts)

with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
