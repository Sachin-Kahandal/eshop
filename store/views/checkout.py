from django.shortcuts import redirect, render
from store.models import Customer
from store.models import Product
from store.models import Order 
from django.views import View


class Checkout(View):
    def get(self, request):
        # if customer is already logged in
        if request.session.get('customer_id'):
            # getting current customer_id from session
            customer_id = request.session.get('customer_id')
            cart = request.session.get('cart')
            # getting the objects 
            customer = Customer.objects.get(id = customer_id)
            products = Product.get_products_byId(list(cart.keys()))
            # setting values
            for product in products:
                order = Order(customer_name=customer,
                product=product, quantity=cart.get(str(product.id)), price = product.price, 
                address=customer.address, phone=customer.phone )
                # placing order
                order.place_order()
            # clearing the cart
            request.session['cart'] = {}
            return redirect('orders')
        else:
            return redirect('login')