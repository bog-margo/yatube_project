from django.shortcuts import render, get_object_or_404
from .models import Post, Group

#Главная страница
def index(request):
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Главная страница'
    text = 'Последние обновления на сайте'
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
        'title': title,
        'text': text,
    }
    return render(request, 'posts/index.html', context) 


def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект 
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'group': group,
        'posts': posts,
    }
    # Третьим параметром передаём словарь context
    return render(request, 'posts/group_list.html', context)