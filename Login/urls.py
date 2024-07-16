# Login/urls.py
from django.urls import path, include
from accounts.views import CustomLoginView, HomeView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),  # URL padrão para o login
    path('home/', HomeView.as_view(), name='home'),
    path('accounts/', include('accounts.urls')),  # Inclui as URLs do aplicativo 'accounts'
    # Outras URLs do seu projeto
]
