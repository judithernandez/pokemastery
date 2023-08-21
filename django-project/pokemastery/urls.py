"""
URL configuration for pokemastery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from . import views # import views.py from the same directory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.greetings, name='greetings'), # static URL
    path('pokepedia/', views.pokepedia, name='pokepedia'), # static URL
    path('pokepedia/<pokemon>', views.index, name='index'), # dynamic URL

]
