# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib.auth.hashers import make_password, check_password
# from .models.product import Product
# from .models.category import Category
# from .models import Customer
# from django.views import View


# # Create your views here.
# def index(request):
#     # To display category specific products
#     categoryId = request.GET.get('category')
#     if categoryId:
#         products = Product.get_all_products_by_categoryid(categoryId)
#     else:
#         # Displays all product, when no category is chosen
#         products = Product.get_all_products()

#     # Displays all categories 
#     categories = Category.get_all_categories()
#     data = {}
#     data['title'] = 'Home'
#     data['products'] = products
#     data['categories'] = categories
#     return render(request, 'index.html', data)


# class Signup(View):
#     def get(self, request):
#         title = {'title':'Sign Up'}
#         return render(request, 'signup.html', title)

#     def post(self,request):
#         post_data = request.POST
#         first_name = post_data.get('first_name')
#         last_name = post_data.get('last_name')
#         phone = post_data.get('phone')
#         email = post_data.get('email')
#         passwd = post_data.get('password')
#         conf_passwd = post_data.get('confirm_password')

#         data = dict()
#         if passwd == conf_passwd:
#             # encrypting password
#             passwd = make_password(passwd)
#             # creating object of Customer class 
#             customer = Customer(first_name = first_name, 
#                 last_name = last_name, phone = phone, email = email, password = passwd)
#             # validating customers email and phone
#             error_msg = self.validate_customer(customer)

#             if error_msg == None:
#                 # customer validated and is registered
#                 customer.register()
#                 return redirect('index')
#             else:
#                 data['error_msg'] = error_msg
#         else:
#             data['error_msg'] = 'Passwords dont match !!!'

#         data['title'] = 'Sign Up'
#         return render(request, 'signup.html',data)
        
               
#     def validate_customer(self, customer):
#         error_msg = None
#         phone_exists = customer.phoneExists() 
#         email_exists = customer.emailExists() 
#         # checking if email and phone is already taken or what
#         if email_exists == False:
#             if phone_exists == False:
#                 return None
#             else:
#                 error_msg = 'Phone already taken !!!'
#         else:
#             error_msg = 'Email already taken !!!'
#         return error_msg


# class Login(View):
#     def get(self, request):
#         data = {'title':'Login'}
#         return render(request, 'login.html', data)

#     def post(self, request):
#         email = request.POST.get('email')
#         passwd = request.POST.get('password')
#         data = dict()

#         customer = Customer.get_customer_email(email)
#         # checking if user exists with same email
#         if customer != None:
#             # checking password
#             flag = check_password(passwd,customer.password)
#             if flag:
#                 # if passwords do match
#                 return redirect('index')
#             else:
#                 data['error_msg'] = 'Wrong usename or password'
#         else:
#             data['error_msg'] = 'Wrong usename or password'
        
#         data['title'] = 'Login'
#         return render(request, 'login.html', data)