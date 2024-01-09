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
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MDQ3OTU3NDYsImV4cCI6MTcwNDc5OTM0Niwicm9sZXMiOlsiUk9MRV9VU0VSIl0sInVzZXJuYW1lIjoicGF1bGsifQ.PKSwaWLQpdGre-dLpDvz4I0DifLoYTqoQ1OC5szA0Txr9F3YcR9DXejuSm4SK2SKgUVZBjyV1-XI3IWjkBjLESv7jDc1tiWF9V3sJpYYW9OtKckgD1FFpCMT97SMhXqt83iptlFYraFsLZKkjrCr6hEKkunzVSHESZYEf0yrEnXl-VW_rBoIIpMER7E3A4lJBPX9qTvkSJ4UOiCCxEFzmX8CEVo7JBd7EIa52ViZlYmSzjSuiCH3eItSONhuIcZkgGKosdTn7Eq51vAC9TB--g2hXf8Em6QNj69UGpzGUX4R_xgTHnk_w0nqzEGS9iRokwQShQ8bJ9C3L1II-VRjhw"
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