
from django import forms
from django.contrib.auth.models import User

class AuthenticateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password', )

    username = forms.CharField(
        max_length=200, 
        required=True, 
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={'class':'form-control', 'type': 'password'})
    )
    
class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password', 'email')

    username = forms.CharField(
        max_length=200, 
        required=True, 
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={'class':'form-control', 'type': 'password'})
    )

    email = forms.EmailField(
        required=True, 
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'email'})
    )
    
    