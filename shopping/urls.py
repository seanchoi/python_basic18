from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('store_admin/', views.adminIndex),
    path('orderprocess/', views.orderProcess),
    path('add_product/process/', views.addProduct),
    path('add_price/process/', views.addPrice),
    path('order_complete/<int:product_id>', views.orderComplete)

]