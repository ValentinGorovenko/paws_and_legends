from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

data_db = [
    {'id': 1, 'title': 'Белка и Стрелка', 'content': 'История о Белке и Стрелке', 'is_published': True},
    {'id': 2, 'title': 'Хатико', 'content': 'Легенда о Хатико', 'is_published': True},
    {'id': 3, 'title': 'Овца Долли', 'content': 'Статья о Овце Долли', 'is_published': False},
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


def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('sport',))
        return HttpResponsePermanentRedirect(uri)

    return HttpResponse(f"<h1>Архив по годам</h1><p >{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
