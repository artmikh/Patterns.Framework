from templator import render
# import settings
from urls import AppRoute, routes
from сreational_patterns import Engine, Logger
from datetime import date
from debug import Debug


site = Engine()
logger = Logger('main')


@AppRoute(routes=routes, url='/')
class Index:
    @Debug(name='Index')
    def __call__(self, request):
        # print(request)
        return '200 OK', render(
            'index.html',
            data=request.get('data', None),
            objects_list=site.categories
            )


@AppRoute(routes=routes, url='/about/')
class About:

    def __call__(self, request):
        # print(request)
        return '200 OK', render('about.html')


@AppRoute(routes=routes, url='/contacts/')
class Contacts:

    def __call__(self, request):
        # print(request)
        return '200 OK', render('contacts.html')


@AppRoute(routes=routes, url='/study_programs/')
class StudyPrograms:
    def __call__(self, request):
        return '200 OK', render(
            'study-programs.html',
            data=date.today(),
            objects_list=site.categories
            )


@AppRoute(routes=routes, url='/courses-list/')
class CoursesList:
    def __call__(self, request):
        logger.log('Список курсов')
        try:
            category = site.find_category_by_id(
                int(request['request_params']['id'])
                )
            return '200 OK', render(
                'courses_list.html',
                objects_list=category.courses,
                name=category.name,
                id=category.id
                )
        except KeyError:
            return '200 OK', 'No courses have been added yet'


@AppRoute(routes=routes, url='/create-course/')
class CreateCourse:
    category_id = -1

    def __call__(self, request):
        if request['method'] == 'POST':
            # метод пост
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))

                course = site.create_course('record', name, category)
                site.courses.append(course)

            return '200 OK', render(
                'courses_list.html',
                objects_list=category.courses,
                name=category.name,
                id=category.id
                )

        else:
            try:
                self.category_id = int(request['request_params']['id'])
                category = site.find_category_by_id(int(self.category_id))

                return '200 OK', render(
                    'create_course.html',
                    name=category.name,
                    id=category.id
                    )
            except KeyError:
                return '200 OK', 'No categories have been added yet'


@AppRoute(routes=routes, url='/create-category/')
class CreateCategory:
    def __call__(self, request):

        if request['method'] == 'POST':
            # метод пост
            # print(request)
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category_id = data.get('category_id')

            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))

            new_category = site.create_category(name, category)

            site.categories.append(new_category)

            return '200 OK', render(
                'index.html',
                objects_list=site.categories
                )
        else:
            categories = site.categories
            return '200 OK', render(
                'create_category.html',
                categories=categories
                )


@AppRoute(routes=routes, url='/category-list/')
class CategoryList:
    def __call__(self, request):
        logger.log('Список категорий')
        return '200 OK', render(
            'category_list.html',
            objects_list=site.categories
            )


@AppRoute(routes=routes, url='/copy-course/')
class CopyCourse:
    def __call__(self, request):
        request_params = request['request_params']

        try:
            name = request_params['name']
            old_course = site.get_course(name)
            if old_course:
                new_name = f'copy_{name}'
                new_course = old_course.clone()
                new_course.name = new_name
                site.courses.append(new_course)

            return '200 OK', render(
                'courses_list.html',
                objects_list=site.courses
                )
        except KeyError:
            return '200 OK', 'No courses have been added yet'


class Not_found_404:

    def __call__(self, request):
        # print(request)
        return '404 WHAT', render('404.html')


@AppRoute(routes=routes, url='/debug/')
class DebugApp:

    def __call__(self, request):
        # print(request)
        from run import Run
        from main import DebugApplication
        from front_controller import fronts
        start_debug = Run(DebugApplication(routes, fronts), 8001)
        return '200 OK', render(
                'debug.html',
                data='debug'
                )
        # return start_debug


@AppRoute(routes=routes, url='/fake/')
class FakeApp:

    def __call__(self, request):
        # print(request)
        from run import Run
        from main import FakeApplication
        from front_controller import fronts
        start_fake = Run(FakeApplication(routes, fronts), 8002)

@AppRoute(routes=routes, url='/original/')
class OriginalApp:

    def __call__(self, request):
        # print(request)
        from run import Run
        from main import Application
        from front_controller import fronts
        start_fake = Run(Application(routes, fronts), 8000)
