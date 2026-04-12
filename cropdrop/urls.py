from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('farmer-dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('add-product/', views.add_product, name='add_product'),
    path('products/', views.product_list, name='product_list'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('place-order/<int:id>/', views.place_order, name='place_order'),
    path('orders/', views.orders, name='orders'),
    path('update-order-status/<int:id>/', views.update_order_status, name='update_order_status'),
    path('delete-product/<int:id>/', views.delete_product, name='delete_product'),
    path('remove-from-cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),  # optional
    path('payment/<int:id>/', views.payment_method, name='payment_method'),
]