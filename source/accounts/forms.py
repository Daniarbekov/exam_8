from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Логин')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким логином не зарегистрирован!')

        user = get_user_model().objects.get(username=username)
        if user and not user.check_password(password):
            raise forms.ValidationError('Неверный пароль!')
