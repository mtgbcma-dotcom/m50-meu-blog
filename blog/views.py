from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_at__lte=timezone.now()).select_related("author")
    return render(request, "blog/post_list.html", {"posts": posts})
