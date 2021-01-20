from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


class Index(View):
    def get(self,request):
        # to set an empty cart in session
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        # To display category specific products
        categoryId = request.GET.get('category')
        if categoryId:
            products = Product.get_all_products_by_categoryid(categoryId)
        else:
            # Displays all product, when no category is chosen
            products = Product.get_all_products()

        # Displays all categories 
        categories = Category.get_all_categories()
        data = {}
        
        data['title'] = 'Home'
        data['products'] = products
        data['categories'] = categories
        return render(request, 'index.html', data)

    def post(self, request):
        product_id = request.POST.get('product_id')
        remove = request.POST.get('remove')
        # accessing session
        cart = request.session.get('cart')
        # if session exist
        if cart:
            quantity = cart.get(product_id)
            # checking if the product already exists in the cart
            if quantity:
                if remove:
                    cart[product_id] = quantity - 1
                    if cart[product_id] == 0:
                        cart.pop(product_id)
                else:    
                    # if exists, inreasing qty by 1
                    cart[product_id] = quantity + 1
            else:    
                # if dosent exist, setting new
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1
        # saving the session 
        request.session['cart'] = cart
        return redirect('index')