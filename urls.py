# from views import *


routes = {}
# routes = {
#     '/': Index(),
#     '/about/': About(),
#     '/contacts/': Contacts(),
#     '/study_programs/': StudyPrograms(),
#     '/courses-list/': CoursesList(),
#     '/create-course/': CreateCourse(),
#     '/create-category/': CreateCategory(),
#     '/category-list/': CategoryList(),
#     '/copy-course/': CopyCourse()
# }


# структурный паттерн - Декоратор, создающий путь урла для контроллера
class AppRoute:

    def __init__(self, routes, url):
        self.routes = routes
        self.url = url

    def __call__(self, cls):
        self.routes[self.url] = cls()
