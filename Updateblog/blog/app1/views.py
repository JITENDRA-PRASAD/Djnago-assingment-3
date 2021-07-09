from django import views
from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.generic.base import TemplateView
from .models import Author,Post,Comment,Tag
from .forms import PostForm, CommentForm
from django.views import View

# Create your views here.


class AddPost(View):
    def get(self, request):
        form = PostForm()
        return render(request,"app1/addpost.html",{
            "forms" : form
        })

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"app1/thanks.html")
        return render(request,'app1/addpost.html',{
            'forms':form
        })


"""
class LogIn(View):
    def get(self,request):
        form = LogInForm()
        return render(request,'app1/login.html',{
            "forms": form
        })

    def post(self,request):
        form = LogInForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"app1/thanks.html")
        return render(request,'app1/login.html',{
            'forms':form
        })

class SingUp(View):
    def get(self,request):
        form = SingUpForm()
        return render(request,"app1/singup.html",{
            "forms":form
        })

    def post(self,request):
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"app1/thanks.html")
        return render(request,"app1/singup.html")
"""

class Comment(View):
    def get(self,request):
        comment = CommentForm()
        return render(request,'app1/commentform.html',{
            'forms':comment
        })

    def post(self,request):
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment.save()
            return render(request,"app1/thanks.html")
        comment = CommentForm()
        return render(request,"app1/commentform.html",{
            "forms":comment
        })

class starting_page(View):
    def get(self,request):
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

