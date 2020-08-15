from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('details/<str:pk>', views.details, name="details"),
    path('checkout/', views.checkout, name="checkout"),
    path('search/', views.search, name="search"),

    path('update/', views.updateItem, name="update_item"),
    path('remove/', views.remove_item, name="remove_item"),

    path('process/', views.process_order, name="process"),

]
