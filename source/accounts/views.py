from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from accounts.forms import LoginForm
from django.contrib.auth import get_user_model
from accounts.forms import UserRegistrationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse


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


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserRegistrationForm
    success_url= '/'
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        context = {}
        context['form'] = form
        return self.render_to_response(context)


class UserView(DetailView):
    template_name = 'user_detail.html'
    model = get_user_model()
    context_object_name = 'user_obj'
    
    
class UserChangeView(UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    
    def get_success_url(self):
        return reverse('account', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(UpdateView):

    model = get_user_model()
    template_name = 'password_change.html'
    form_class = PasswordChangeForm
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('login')
