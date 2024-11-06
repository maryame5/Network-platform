
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_post",views.create_post,name="create_post"),
    path("profil/<str:name>", views.profil ,name="profil"),
    path("follow/<str:following_name>", views.follow_fun ,name="follow"),
    path("following/", views.following ,name="following"),
    path("edit_post/<int:postId>", views.edit ,name="edit"),
    path("post/<int:postId>", views.get_post ,name="post"),
    path("like/<int:postId>", views.up_like ,name="like"),
]