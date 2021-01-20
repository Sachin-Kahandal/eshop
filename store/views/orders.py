from django.shortcuts import redirect, render
from store.models import Customer
from store.models import Product
from store.models import Order 
from django.views import View


class Orders(View):
    def get(self, request):
        customer_id = request.session.get('customer_id')
        if customer_id:
            orders = Order.get_orders(customer_id)
            data = dict()
            data['title'] = 'Orders'
            data['orders'] = orders
            return render(request, 'orders.html', data)
        else:
            return_url = request.META['PATH_INFO']
            return redirect(f'login?return_url={return_url}')