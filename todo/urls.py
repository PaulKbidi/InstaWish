from django.urls import path

from.import views

urlpatterns = [
    path("unfollow/<int:pk>",views.unfollow_page_todo,name="todo-unfollow-url"),
    path("follow/<int:pk>",views.follow_page_todo,name="todo-follow-url"),
    path("post/<int:pk>",views.post_page_todo,name="todo-post-url"),
    path("user_post/<int:pk>",views.user_post_page_todo,name="todo-user-post-url"),
    path("user/<int:pk>",views.user_page_todo,name="todo-user-url"),
    path("own",views.own_page_todo,name="todo-own-url"),
    path("",views.starting_page_todo,name="todo-starting-url"),
    path("register",views.register_page_todo,name="todo-register-url"),
    path("login",views.login_page_todo,name="todo-login-url"),
]