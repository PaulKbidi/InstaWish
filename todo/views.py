from django.shortcuts import render
from django.template import context
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
import requests
import json
from .forms import LoginForm, RegisterForm, ListeForm
# Create your views here.

def starting_page_todo(request):
    # reqUrl = "http://127.0.0.1:8000/api/listes"

    response = requests.request("GET", reqUrl)
    data = response.json()
    context={"response":data}
    return render(request, "todo/index.html", context=context)

def create_listes_page_todo(request):
    # reqUrl = "http://127.0.0.1:8000/api/listes"

    if request.method == 'POST':
        form = ListeForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data["name"]
            print(name)
            
            headersList = {
                "Accept": "*/*",
                "User-Agent": "Thunder Client (https://www.thunderclient.com)",
                "Content-type": "application/ld+json",
                "Authorization": "Bearer" 
            }
            payload = json.dumps({
                "name": name
            })
            response = requests.request("POST", reqUrl, data=payload,  headers=headersList)
            print(response)
            return render(request, "todo/index.html")
    else:
        form = ListeForm()
    return render(request, "todo/create_liste.html", {'form':form})

def tasks_page_todo(request):
    # reqUrl = "http://127.0.0.1:8000/api/tasks"

    response = requests.request("GET", reqUrl)
    data = response.json()
    context={"response":data}
    return render(request, "todo/tasks.html", context=context)

def login_page_todo(request):
    reqUrl = "https://symfony-instawish.formaterz.fr/api/login_check"

    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["current_username"]
            password = form.cleaned_data["current_password"]
            print(username)
            print(password)
            
            headersList = {
                "Accept": "*/*",
                "User-Agent": "Thunder Client (https://www.thunderclient.com)",
                "Content-type": "application/ld+json" 
            }
            payload = json.dumps({
                "username": username,
                "password": password
            })
            response = requests.request("POST", reqUrl, data=payload,  headers=headersList)
            datas = response.json()
            context={"token":datas}
            print(datas)
            return render(request, "todo/index.html", context=context)
    else:
        form = LoginForm()
    return render(request, "todo/login.html", {'form':form})

def register_page_todo(request):
    reqUrl = "https://symfony-instawish.formaterz.fr/api/register"

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            username = form.cleaned_data["username"]
            print(email)
            print(password)
            print(username)
            
            post_files = {
                "profilePicture": open((request.FILES["profilePicture"]), "rb"),
            }
            
            headersList = {
                "Accept": "*/*",
                "User-Agent": "Thunder Client (https://www.thunderclient.com)",
                "Content-Type": "multipart/form-data; boundary=kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A" 
            }
            
            payload = "--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; name=\"email\"\r\n\r\n",email,
            "\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n",password,
            "\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n",username,
            "\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A--\r\n"
            
            response = requests.request("POST", reqUrl, data=payload, headers=headersList, files=post_files)
            print(response.text)
            return render(request, "todo/index.html")
    else:
        form = RegisterForm()
    return render(request, "todo/register.html", {'form':form})