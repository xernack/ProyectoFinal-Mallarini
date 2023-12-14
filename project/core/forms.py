#### REGISTRO
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel

class UserCreationFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
      model = UserModel
      fields = ["password1", "password2", "username", "email"]
      help_texts = {k: "" for k in fields}
