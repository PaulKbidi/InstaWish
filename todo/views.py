from django.shortcuts import render
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

    headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MDQ3OTk2NzYsImV4cCI6MTcwNDgwMzI3Niwicm9sZXMiOlsiUk9MRV9VU0VSIl0sInVzZXJuYW1lIjoicGF1bGsifQ.iRp2QOpxS3LPo7aAFoYVcUopf-62MAFkOW8sMyEiqR1P9AmKKf6GLA56RWtJViifdEMTGTJas9gM0s6rdTZnyEar2h5BATN7ET87Scx-9rCsfmgIYO9t7jSlbjKKPPet-lMNnZwN_J4KSRXaZw7F__2NTiPihDgbu6J9vcmXoN7y2vOrolZL8FCvbi85Xnxyc4X6pajMmCmSml0oV4OsitgpRi6JA5FcmwDbc7hMjBRZKbQ30i-fXj93kFFgZXjebxeBGgqUnB9mqz84S3odyJ4AMT5ZTOjqgfTgKWUWzMvdEN0TRaFkzKaOkTwojVH_2jsf2o3TdaqPuGtkfuTwvQ"
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload, headers=headersList)

    data = response.json
    return render(request, "todo/index.html", {'data':data})

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
            response = requests.post(reqUrl, data=payload,  headers=headersList)
            if response.status_code ==200:
                token_data = response.json()
                token = token_data.get('token', None)
                if token:
                    request.session['api_token'] = token
                    print(token)
                    return render(request, "todo/index.html")
                else:
                    return JsonResponse({"message": "Erreur: Aucun token trouvé dans la réponse de l'API"})
            else :
                return JsonResponse({"message": f"Erreur: {response.status_code} - {response.text}"}, status=response.status_code)
        return render(request, "todo/index.html")
    else:
        form = LoginForm()
    return render(request, "registration/login.html", {'form':form})

import requests
from django.http import JsonResponse

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
            
            print(response.text)
            
            return render(request, "todo/index.html")
    else:
        form = RegisterForm()
    
    return render(request, "todo/register.html", {'form': form})

