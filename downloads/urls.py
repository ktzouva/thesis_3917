from django.urls import path
from . import views

app_name = 'downloads'

urlpatterns = [
    path('', views.downloads_home, name = 'downloads_home'),
]
