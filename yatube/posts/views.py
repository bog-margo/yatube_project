from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def index(request):
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = 'posts/index.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    text = 'Это главная страница проекта Yatube'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'text': text,
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


def group_posts(request, pk):
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = 'posts/group_list.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    text_for_posts = 'Здесь будет информация о группах проекта Yatube'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'text_for_posts': text_for_posts,
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context, pk)