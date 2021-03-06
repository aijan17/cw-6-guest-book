"""guest_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from webapp.views import guest_list, get_search, create_guest, update_view, remove_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', guest_list, name='guest-list'),
    path('search/', get_search, name='search'),
    path('add/', create_guest, name='add'),
    path('update/<int:id>', update_view, name='update'),
    path('remove/<int:id>', remove_view, name='delete'),


]
