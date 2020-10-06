from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



# Фреймворк аутентификации Django предоставляет форму
# с именем UserCreationForm(которая наследуется от ModelFormкласса)
# для обработки создания новых пользователей. Он имеет три поля,
# а именно username, password1и password2(для подтверждения пароля).
# По этому мы добавили дополнительно email

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username', 'password1', 'password2', 'email']

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
