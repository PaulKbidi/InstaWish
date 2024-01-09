from django.urls import path

from.import views

urlpatterns = [
    path("create_liste",views.create_listes_page_todo,name="todo-create-liste-url"),
    path("register",views.register_page_todo,name="todo-register-url"),
    path("login",views.login_page_todo,name="todo-login-url"),
    path("tasks",views.tasks_page_todo,name="todo-tasks-url"),
    path("",views.starting_page_todo,name="todo-starting-url"),
]