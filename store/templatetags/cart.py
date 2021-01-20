from django import template

# decorator
register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    if str(product.id) in cart:
        return True    
    else:
        return False

@register.filter(name='cart_qty')
def cart_qty(product, cart):
    return cart.get(str(product.id)) 
    

@register.filter(name="price_total")
def price_total(product, cart):
    return product.price * cart_qty(product, cart)


@register.filter(name='cart_total')
def cart_total(products, cart):
    sum = 0
    for product in products:
        sum = sum + price_total(product, cart)
    return sum

@register.filter(name='currency')
def currency(no):
    return "₹ " + str(no) 

@register.filter(name="order_total")
def order_total(num1, num2):
    return num1 * num2