from django.shortcuts import render, redirect
from django.template import context
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
import requests
from django.http import JsonResponse
import json
from .forms import LoginForm, RegisterForm
# Create your views here.

def starting_page_todo(request):
    reqUrl = "https://symfony-instawish.formaterz.fr/api/users"
    
    api_token = request.session.get('api_token')
    if api_token == None:
        return redirect('todo-login-url')
    else :
        headersList = {
            "Accept": "*/*",
            "User-Agent": "Thunder Client (https://www.thunderclient.com)",
            "Authorization": "Bearer " + api_token
        }

        payload = ""

        response = requests.request("GET", reqUrl, data=payload, headers=headersList)

        data = response.json
        return render(request, "todo/index.html", {'data':data})

def user_page_todo(request, pk):
    id = str(pk)
    reqUrl = "https://symfony-instawish.formaterz.fr/api/user/"+id
    print (reqUrl)
    
    api_token = request.session.get('api_token')
    print(api_token)

    headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "Authorization": "Bearer " + api_token
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload, headers=headersList)

    data = response.json
    return render(request, "todo/user.html", {'data':data})

def user_post_page_todo(request, pk):
    id = str(pk)
    reqUrl = "https://symfony-instawish.formaterz.fr/api/home/"+id
    print (reqUrl)
    
    api_token = request.session.get('api_token')
    print(api_token)

    headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "Authorization": "Bearer " + api_token
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload, headers=headersList)
    
    data = response.json
    return render(request, "todo/user_post.html", {'data':data})

def post_page_todo(request, pk):
    id = str(pk)
    reqUrl = "https://symfony-instawish.formaterz.fr/api/liked/"+id
    print (reqUrl)
    
    api_token = request.session.get('api_token')
    print(api_token)

    headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "Authorization": "Bearer " + api_token
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload, headers=headersList)
    
    print('__________________________________' + response.text)
    return redirect('todo-user-post-url', pk = pk)

def follow_page_todo(request, pk):
    api_token = request.session.get('api_token')
    id = str(pk)
    reqUrl = "https://symfony-instawish.formaterz.fr/api/follow/add/"+id

    headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "Authorization": "Bearer " + api_token
    }

    payload = ""

    response = requests.request("POST", reqUrl, data=payload,  headers=headersList)
    print(response.text)
    return redirect("todo-user-url", pk = pk)

def unfollow_page_todo(request, pk):
    api_token = request.session.get('api_token')
    id = str(pk)
    reqUrl = "https://symfony-instawish.formaterz.fr/api/follow/remove/"+id

    headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "Authorization": "Bearer " + api_token
    }

    payload = ""

    response = requests.request("POST", reqUrl, data=payload,  headers=headersList)
    print(response.text)
    return redirect("todo-user-url", pk = pk)

def own_page_todo(request):
    reqUrl = "https://symfony-instawish.formaterz.fr/api/me"
    
    api_token = request.session.get('api_token')
    print(api_token)

    headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "Authorization": "Bearer " + api_token
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

    data = response.json
    print(data)
    return render(request, "todo/own.html", {'data':data})

def login_page_todo(request):
    reqUrl = "https://symfony-instawish.formaterz.fr/api/login_check"

    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["current_username"]
            password = form.cleaned_data["current_password"]
            
            headersList = {
                "Accept": "*/*",
                "User-Agent": "Thunder Client (https://www.thunderclient.com)",
                "Content-type": "application/ld+json" 
            }
            payload = json.dumps({
                "username": username,
                "password": password
            })
            response = requests.post(reqUrl, data=payload,  headers=headersList)
            if response.status_code == 200:
                token_data = response.json()
                token = token_data.get('token', None)
                if token:
                    request.session['api_token'] = token
                    return redirect('todo-starting-url')
                else:
                    return JsonResponse({"message": "Erreur: Aucun token trouvé dans la réponse de l'API"})
            else :
                return JsonResponse({"message": f"Erreur: {response.status_code} - {response.text}"}, status=response.status_code)
        else :
            return render(request, "todo/index.html")
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
            
            post_files = {
                "profilePicture": request.FILES["profilePicture"],
            }
            
            headersList = {
                "Accept": "*/*",
                "User-Agent": "Thunder Client (https://www.thunderclient.com)",
            }
            
            payload = {
                "email": email,
                "password": password,
                "username": username,
            }

            response = requests.post(reqUrl, headers=headersList, data=payload, files=post_files)
            
            return render(request, "todo/index.html")
    else:
        form = RegisterForm()
    
    return render(request, "todo/register.html", {'form': form})

