"""
URL configuration for marshall project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from marshallweb import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('nightclubs/', views.nightclubs, name='nightclubs'),
    path('date/<str:day>', views.date, name='date'),
    path('contact/', views.contact, name='contact'),
    path('photos/', views.photos, name='photos'),
    path('pacha/', views.pacha, name='pacha'),
    path('otto/', views.otto, name='otto'),
    path('opium/', views.opium, name='opium'),
    path('downtown/', views.downtown, name='downtown'),
    path('biblio/', views.biblio, name='biblio'),
    path('cookies/', views.cookies, name='cookies'),
    
    
]
