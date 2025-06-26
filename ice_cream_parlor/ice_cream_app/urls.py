# cafe/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.flavor_list, name='flavor_list'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:flavor_id>/', views.add_to_cart, name='add_to_cart'),
    path('suggest/', views.suggest_flavor, name='suggest_flavor'),
    path('add-allergen/', views.add_allergen, name='add_allergen'),
]
