from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render

from .models import Animal

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
cats_db = [
    {'id': 1, 'name': 'Домашние животные'},
    {'id': 2, 'name': 'Дикие животные'},
]


def index(request):
    posts = Animal.objects.filter(is_published=1)
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': posts,
            'cat_selected': 0,
            }
    return render(request, 'animals/index.html', data)


def about(request):
    data = {'title': 'О сайте',
            'menu': menu}
    return render(request, 'animals/about.html', data)


def show_post(request, post_slug):
    post = get_object_or_404(Animal, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }

    return render(request, 'animals/post.html', context=data)


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }

    return render(request, 'animals/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
