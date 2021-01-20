from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models import Customer
from django.views import View


class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        data = {'title':'Login'}
        return render(request, 'login.html', data)      

    def post(self, request):
        email = request.POST.get('email')
        passwd = request.POST.get('password')
        data = dict()

        customer = Customer.get_customer_email(email)
        # checking if user exists with same email
        if customer != None:
            # checking password
            flag = check_password(passwd,customer.password)
            if flag:
                # setting up session upon succesful log in
                request.session['customer_id'] = customer.id
                request.session['customer_email'] = customer.email
                # if passwords do match
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('index')
            else:
                data['error_msg'] = 'Wrong usename or password'
        else:
            data['error_msg'] = 'Wrong usename or password'
        
        data['title'] = 'Login'
        return render(request, 'login.html', data)
        
   
def logout(request):
    request.session.clear()
    return redirect('index')