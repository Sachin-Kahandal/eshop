from django.shortcuts import redirect, render
from store.models import Customer
from store.models import Product
from django.views import View


class Cart(View):
    def get(self, request):
        cart_val = list(request.session.get('cart').keys())
        products_cart = Product.get_products_byId(cart_val)
        data = {}
        data['title'] = 'Cart'
        data['products'] = products_cart
        return render(request,'cart.html', data)