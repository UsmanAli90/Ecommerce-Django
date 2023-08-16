from django import template

register=template.Library()


#Using filter to check if the specific product is add to cart or not

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==product.id:
            return True
    # print(keys)
    # print(product,cart)
    return False



@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==product.id:
            return cart.get(id)
    # print(keys)
    return 0


@register.filter(name='price_total')
def price_total(product,cart):
    return product.price*cart_quantity(product,cart)



@register.filter(name='total_cart_price')
def total_cart_price(product,cart):
    sum=0
    for p in product:
        sum+=price_total(p,cart)
    
    return sum