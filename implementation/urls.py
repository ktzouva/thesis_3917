from django.urls import path
from implementation.views import ImplementationView

app_name = 'implementation'

urlpatterns = [
    path('', ImplementationView.as_view(), name = 'implementation_home'),
]
