from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.generic import TemplateView
from accounts.forms import LoginForm
from django.contrib.auth import get_user_model


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
        else:
            form = LoginForm(request.POST)
        return self.render_to_response(context={'form':form})


def logout_view(request):
    logout(request)
    return redirect('index')
