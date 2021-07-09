from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page.as_view(), name="starting-page"),
    path("posts/", views.posts, name="all-posts"),
    path("posts/<slug:post_slug>", views.post_detail, name="selected-post"),
    path("addpost/", views.AddPost.as_view() , name='addpost'),
    #path("login/",views.LogIn.as_view(),name="login"),
    #path("singup/",views.SingUp.as_view(), name="singup"),
    path("comment/",views.Comment.as_view(), name="comment"),
]