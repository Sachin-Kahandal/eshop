from django.db import models
from .product import Product
from .customer import Customer
import datetime

class Order(models.Model):
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    completed = models.BooleanField(default=False)
    
    def place_order(self):
        self.save()

    @staticmethod
    def get_orders(customer_id):
        orders = Order.objects.filter(customer_name_id = customer_id).order_by('-id')
        return orders