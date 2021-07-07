from django.shortcuts import render
from django.http import HttpResponseNotFound
from datetime import date
from .models import Author,Post,Comment,Tag
from .forms import PostForm

# Create your views here.

def get_date(post):
    date = Post.date
    return post['date']

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "app1/index.html", {
        "posts": latest_posts
    })

def posts(request):
    all_post = Post.objects.all()
    return render(request, "app1/all_posts.html", {
        "posts": all_post
    })

def post_detail(request, post_slug):
    selected_post = Post.objects.get(slug=post_slug)
    if selected_post:
        return render(request, "app1/post_detail.html", {
            "post": selected_post
        })
    else:
        return HttpResponseNotFound("Post Not Found")

def LogIn(request):
    form = PostForm()
    if request.method == 'POST':
        return render(request,"app1/login.html",{
            'forms':form
        })
    return render(request,'app1/login.html',{
        'forms':form
    })