from templator import render
import settings


class Index:

    def __call__(self, request):
        print(request)
        return '200 OK', render(
            'index.html',
            data=request.get('data', None),
            css=settings.css_file
            )


class About:

    def __call__(self, request):
        print(request)
        return '200 OK', render('about.html', css=settings.css_file)


class Contacts:

    def __call__(self, request):
        print(request)
        return '200 OK', render('contacts.html', css=settings.css_file)


class Not_found_404:

    def __call__(self, request):
        print(request)
        return '404 WHAT', render('404.html', css=settings.css_file)

