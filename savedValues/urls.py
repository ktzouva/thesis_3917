from django.urls import path
from . import views as views

app_name = 'savedValues'

urlpatterns = [
    path('', views.savedValues_home, name = 'savedValues_home'),
]
