from django.contrib import admin
from django.urls import path, include
from . import views as views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('downloads/', include('downloads.urls')),
    path('algorithms/', include('algorithms.urls')),
    path('implementation/', include('implementation.urls')),
    path('saved_values/', include('savedValues.urls')),
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/', include('accounts.urls')),
    path('datamng/', include('datamng.urls')),
]

urlpatterns += staticfiles_urlpatterns()
