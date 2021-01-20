from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def register(self):
        self.save()
    
    # checks if email exists
    def emailExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        else:
            return False

    # checks if phone exists
    def phoneExists(self):
        if Customer.objects.filter(phone = self.phone):
            return True
        else:
            return False

    @staticmethod
    def get_customer_email(email):
        try:
            customer = Customer.objects.get(email = email)
            return customer
        except:
            return None
