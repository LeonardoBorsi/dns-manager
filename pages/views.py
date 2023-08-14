from django.http import JsonResponse
from django.views import View
from django.views.generic import (TemplateView, FormView)
from django.contrib.auth.views import (LoginView, LogoutView)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth.models import User

from pages.forms import CustomUserCreationForm


class RegisterPageView(FormView):
    template_name = 'user/register.html'
    form_class = CustomUserCreationForm
    success_url = '/login'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class HomePageView(TemplateView):
    template_name='home.html'

class LoginPageView(LoginView):
    template_name='user/login.html'
    next_page='/'

class LogoutPageView(LogoutView):
    next_page='/'

class ProfilePageView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user/profile.html'

    def get_object(self):
        # Ritorna l'utente corrente
        return self.request.user
    
class CreateSuperuserView(View):
    def get(self, request):
        User.objects.create_superuser('usrname', 'email', 'password')
        return JsonResponse({"status": "Superuser created"})