import settings
from jinja2 import FileSystemLoader
from jinja2.environment import Environment


def render(template_name, **kwargs):

    env = Environment()
    # Загружаем папку с шаблонами
    env.loader = FileSystemLoader(settings.TEMPLATES_ROOT)
    # Открываем шаблон по имени
    template = env.get_template(template_name)
    # рендерим шаблон с параметрами
    return template.render(**kwargs)
