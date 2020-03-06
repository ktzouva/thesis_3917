from django.urls import path
from . import views as views
from implementation.views import ImplementationView
#from implementation.views import SavedValuesView

app_name = 'implementation'

urlpatterns = [
    path('', ImplementationView.as_view(), name = 'implementation_home'),
    path('saved_values/', views.SavedValuesView, name = 'saved_values'),
]
