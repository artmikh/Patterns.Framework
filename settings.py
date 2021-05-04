""" Файл с конфигурациями проекта """
import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

""" Адрес папки с шаблонами """
TEMPLATES_ROOT = os.path.join(BASE_DIR, "templates")

""" Тестовая надпись, выводится в консоль, для проверки работы нужного кода """
# Пример запуска settings.TEST(variable_name)
def TEST(variable):
    print(f"It's Alive!!! : {variable}")


""" Путь к статичным файлам (css, font) """
STATIC_URL = '/static/'

STATICFILES_DIRS = (BASE_DIR / "static")


# dir_path = os.path.dirname(os.path.realpath(__file__))
# dir_path = os.getcwd()
