import quopri
from wsgiref.util import setup_testing_defaults
from views import Not_found_404
from requests import GetRequests, PostRequests


class Application:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        setup_testing_defaults(environ)

        path = environ['PATH_INFO']

        # Если в пути нет '/' в конце, то добавляем его
        if not path.endswith('/'):
            path = f'{path}/'

        # Обработка get и post запросов
        request = {}
        # Получаем все данные запроса
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = data
            print(f'Нам пришёл POST-запрос: {Application.decode_value(data)}')
        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = request_params
            print(f'Нам пришли GET-параметры: {Application.decode_value(request_params)}')

        # page controller
        if path in self.routes:
            view = self.routes[path]
        else:
            view = Not_found_404()

        # front controller
        for front in self.fronts:
            front(request)

        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    # Избавление от белеберды
    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data


class DebugApplication(Application):

    def __init__(self, routes_obj, fronts_obj):
        self.application = Application(routes_obj, fronts_obj)
        super().__init__(routes_obj, fronts_obj)

    def __call__(self, env, start_response):
        print('DEBUG MODE')
        print(env)
        return self.application(env, start_response)


class FakeApplication(Application):

    def __init__(self, routes_obj, fronts_obj):
        self.application = Application(routes_obj, fronts_obj)
        super().__init__(routes_obj, fronts_obj)

    def __call__(self, env, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Hello from Fake']
