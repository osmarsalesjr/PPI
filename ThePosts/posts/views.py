from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from posts.forms import *
from posts.models import *


# Create your views here.
def index(request):
    posts = Post.objects.order_by('-data_published')
    return render(request, 'index.html', {'posts': posts})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form.save()
            return redirect('index')
    else:
        form = PostForm()
        return render(request, 'add_post.html', {'form': form})


def post_detail(request, pk):

    post = Post.objects.get(id=pk)
    return render(request, 'post_detail.html', {'post': post})


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.data_modified = timezone.now()
            post.save()
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'edit_post.html', {'form': form})
