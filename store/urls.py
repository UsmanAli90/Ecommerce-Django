# from django.contrib import admin
from django.urls import path
from store.views.home import Index
from store.views.signup import Signup
from store.views.login import Login,logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from store.middlewares.auth import auth_middleware



urlpatterns = [
    path('',Index.as_view(),name='homepage'),
    path('signup',Signup.as_view(),name='signup'),
    path('login',Login.as_view(), name='login'),
    path('logout',logout, name='logout'),
    path('cart',Cart.as_view(), name='cart'),
    path('checkout',CheckOut.as_view(), name='checkout'),
    path('orders',auth_middleware(OrderView.as_view()), name='orders'),
]