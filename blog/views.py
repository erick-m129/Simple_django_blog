from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse



def blog_index(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category)
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=request.user,
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
            return  HttpResponseRedirect(reverse.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "comments": comments,
        "from": form,
        "post": post,
    }
    return render(request, "blog/detail.html", context)



