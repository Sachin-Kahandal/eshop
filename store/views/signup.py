from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        title = {'title':'Sign Up'}
        return render(request, 'signup.html', title)

    def post(self,request):
        post_data = request.POST
        first_name = post_data.get('first_name')
        last_name = post_data.get('last_name')
        phone = post_data.get('phone')
        address = post_data.get('address')
        email = post_data.get('email')
        passwd = post_data.get('password')
        conf_passwd = post_data.get('confirm_password')

        data = dict()
        if len(passwd) > 7:
            if passwd == conf_passwd:
                # encrypting password
                passwd = make_password(passwd)
                # creating object of Customer class 
                customer = Customer(first_name = first_name, 
                    last_name = last_name, phone = phone, address=address, email = email, password = passwd)
                # validating customers email and phone
                error_msg = self.validate_customer(customer)

                if error_msg == None:
                    # customer validated and is registered
                    customer.register()
                    return redirect('login')
                else:
                    data['error_msg'] = error_msg
            else:
                data['error_msg'] = 'Passwords dont match !!!'
        else:
            data['error_msg'] = 'Passwords too short !!!'

        data['title'] = 'Sign Up'
        return render(request, 'signup.html',data)
        
               
    def validate_customer(self, customer):
        error_msg = None
        phone_exists = customer.phoneExists() 
        email_exists = customer.emailExists() 
        # checking if email and phone is already taken or what
        if email_exists == False:
            if phone_exists == False:
                return None
            else:
                error_msg = 'Phone already taken !!!'
        else:
            error_msg = 'Email already taken !!!'
        return error_msg
