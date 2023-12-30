from django.urls import path
# from . views import *
from . views import RegistrationView, LoginView, LogoutView, UserProfileView, password_change, UserProfileUpdateView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('update_profile/', UserProfileUpdateView.as_view(), name='update_profile'),
    path('password_change/', password_change, name='password_change'),
]