from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})
# Мы импортируем модель Post из models.py.
# Функция post_list принимает параметр request.
# Мы получаем все объекты Post, отсортированные по дате создания (от новых к старым).
# Функция render отображает шаблон 'blog/post_list.html', передавая ему контекст с списком постов.