from templator import render


class Index:

    def __call__(self, request):
        print(request)
        return '200 OK', [b'<h1>Index</h1>']


class About:

    def __call__(self, request):
        print(request)
        return '200 OK', [b'<h1>About</h1>']


class Contacts:

    def __call__(self, request):
        print(request)
        return '200 OK', [b'<h1>Contacts</h1>']


class Not_found_404:

    def __call__(self, request):
        print(request)
        return '404 WHAT', [b'<h1>404 PAGE Not Found</h1>']


# Тестовая страница для пробы внедрения шаблонизатора
class Test:
    def __call__(self, request):
        print(request)
        output_test = render(
            'authors.html',
            object_list=[{'name': 'Leo'}, {'name': 'Kate'}]
            )
        return '200 OK', [output_test.encode('utf-8')]
