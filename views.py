from templator import render


class Index:

    def __call__(self, request):
        print(request)
        return '200 OK', render('index.html', data=request.get('data', None))


class About:

    def __call__(self, request):
        print(request)
        return '200 OK', '<h1>About</h1>'


class Contacts:

    def __call__(self, request):
        print(request)
        return '200 OK', '<h1>Contacts</h1>'


class Not_found_404:

    def __call__(self, request):
        print(request)
        return '404 WHAT', '<h1>404 PAGE Not Found</h1>'

