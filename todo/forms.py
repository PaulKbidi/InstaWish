from django import forms


class LoginForm(forms.Form):
    current_username = forms.CharField(label="Username", max_length=100)
    current_password = forms.CharField(label="Password", max_length=32, widget=forms.PasswordInput)
    
class RegisterForm(forms.Form):
    email = forms.CharField(label="Email", max_length=100)
    password = forms.CharField(label="Password", max_length=32, widget=forms.PasswordInput)
    username = forms.CharField(label="Username", max_length=100)
    profilePicture = forms.FileField(label="ProfilePicture")
    
class ListeForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)