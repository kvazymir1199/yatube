from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# Create your views here.
def index(request):
    posts = Post.objects.all()[:10]
    context = {
        "title": "Последние обновления на сайте",
        'posts': posts
    }
    return render(request, "posts/index.html", context=context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    # выведем посты
    posts = group.groups.all()[:10]

    context = {
        "group": group,
        "posts": posts,
        "title": "Лев Толстой – зеркало русской революции."
    }
    return render(request, "posts/group_list.html", context=context)
