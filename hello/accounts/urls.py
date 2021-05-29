from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import register_view, UserDetailView, login_view, logout_view

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create/', register_view, name='create'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
]

