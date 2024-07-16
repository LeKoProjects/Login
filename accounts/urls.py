# accounts/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import HomeView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # outras URLs do seu aplicativo accounts
]
