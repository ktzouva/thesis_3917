from django.urls import path
from . import views

app_name = 'datamng'

urlpatterns = [
    path('', views.datamng_home, name = 'datamng_home'),
    path('runalg/', views.runalg, name = 'runalg'),
]
