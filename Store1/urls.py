"""Store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from APP.views import *
from django.urls import include, path
from APP import views






urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/',page),
    path('',main),
    path('random/',pagewithrandom),
    path('hello',hello),
    path ('products/',include('APP.urls')),
    path('time/', TimePage),
    path('login/', user),
    path('products/', products_view, name= 'products'),
    path('products/<int:id>', product_view, name= 'product' ),
    path('', views.index),
    path('user/', views.user),
    path('img/',file_show),
    path('json/',json_show ),
    path('p1/', p1),
    path('p2/', p2),
    path('welcome/', index),
    path('food/', include('APP.urls2')),
    path('cat/', cat),
    path('dog/', dog),
    path('fish/', fish),
    path('hamster/', hamster),
    path('Cat/',Cat),
    path('Dog', Dog),
    path('Fish', Fish),
    path('Hamster', Hamster)
   



]
