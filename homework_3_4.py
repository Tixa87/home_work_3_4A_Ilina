# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser Chrome"
# или "Open Browser [Chrome]"
# на ваш выбор.

# Функция берет название функции, делает первую букву заглавной, заменяет нижнее подчеркивание на пробел,
# после двоеточия добавляет в вывод аргумент. Завершает предложение точкой.
def decorate(name, *args):
    print(name.__name__.capitalize().replace("_", " ") + ":", *args, ".")


def open_browser(browser_name):
    decorate(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    decorate(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    decorate(find_registration_button_on_login_page, page_url, button_text)


open_browser("Chrome")
go_to_companyname_homepage("qa.guru")
find_registration_button_on_login_page("qa.guru", "Личный кабинет")
