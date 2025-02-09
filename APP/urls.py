from django.urls import path
from .views import *
from APP.views import products_view,product_view
from django.contrib import admin
from APP import views

urlpatterns = [
    path('cat/<int:milkid>/', categorires),
    path('admin/', admin.site.urls),
    path('products/', products_view, name= 'products'),
    path('product/<int:id>', product_view, name= 'product' )



]