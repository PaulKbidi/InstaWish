from django.urls import path

from.import views

urlpatterns = [
    path("register",views.register_page_todo,name="todo-register-url"),
    path("login",views.login_page_todo,name="todo-login-url"),
    path("user/<int:pk>",views.user_page_todo,name="todo-user-url"),
    path("follow/<int:pk>",views.follow_page_todo,name="todo-follow-url"),
    path("own",views.own_page_todo,name="todo-own-url"),
    path("",views.starting_page_todo,name="todo-starting-url"),
]