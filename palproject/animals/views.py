from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]
data_db = [
    {'id': 1, 'title': 'Белка и Стрелка', 'content': 'История о Белке и Стрелке', 'is_published': True},
    {'id': 2, 'title': 'Хатико', 'content': 'Легенда о Хатико', 'is_published': True},
    {'id': 3, 'title': 'Овца Долли', 'content': 'Статья об Овце Долли', 'is_published': False},
]


def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': data_db}
    return render(request, 'animals/index.html', data)


def about(request):
    data = {'title': 'О сайте',
            'menu': menu}
    return render(request, 'animals/about.html', data)


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
