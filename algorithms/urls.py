from django.urls import path
from . import views

app_name = 'algorithms'

urlpatterns = [
    path('', views.algorithms_home, name = 'algorithms_home'),
    path('<slug>/', views.algorithms_detail, name = 'detail'),
]
