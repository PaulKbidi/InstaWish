from django import forms


class LoginForm(forms.Form):
    current_username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder':'Username'})
    )
    current_password = forms.CharField(
        max_length=32, 
        widget=forms.PasswordInput(attrs={'placeholder':'Password'})
    )
    
class RegisterForm(forms.Form):
    email = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder':'Email'})
    )
    password = forms.CharField(
        max_length=32,
        widget=forms.PasswordInput(attrs={'placeholder':'Password'})
    )
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder':'Username'})
    )
    profilePicture = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'inputfile'})
    )
    
class ListeForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)