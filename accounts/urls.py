from django.urls import path
from . import views as views

app_name = 'accounts'

urlpatterns = [
    path('', views.accounts_home, name = 'accounts_home'),
    path('login/', views.login_view, name = 'login'),
    path('signup/', views.signup_view, name = 'signup'),
    path('logout/', views.logout_view, name = 'logout'),
]
