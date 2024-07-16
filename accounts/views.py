# accounts/views.py
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class HomeView(LoginRequiredMixin, View):
    login_url = '/login/'  # URL de login
    redirect_field_name = 'next'  # Parâmetro para redirecionamento após o login

    def get(self, request):
        return render(request, 'accounts/home.html')

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')  # Redireciona para a página inicial após o login

