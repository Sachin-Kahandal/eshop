from django.urls import path, include
from store.views.index import Index
from store.views.signup import Signup
from store.views.login import Login, logout
from store.views.cart import Cart
from store.views.checkout import Checkout
from store.views.orders import Orders

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('checkout', Checkout.as_view(), name='checkout'),
    path('orders', Orders.as_view(), name='orders'),
]