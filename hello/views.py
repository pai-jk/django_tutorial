from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def say_hello(request):
    print("hello")
    return HttpResponse("hello")


def post_list(request):
    posts = Post.objects.all().order_by('created_date')
    #posts = Post.objects.filter(author='author1')
    return render(request, 'hello/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk) #pk값인 경우 get
    return render(request, 'hello/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('hello:post_detail', pk=post.pk)

    elif request.method == "GET":
        form = PostForm()
    else:
        raise ValueError

    return render(request, 'hello/post_new.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('hello:post_detail', pk=post.pk)
        pass
    elif request.method == "GET":
        form = PostForm(instance=post)
        # form = Post.objects.get(pk=pk)

    else:
        raise ValueError
    return render(request, 'hello/post_edit.html', {'form': form})