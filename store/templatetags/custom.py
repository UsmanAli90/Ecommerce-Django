from django import template

register=template.Library()


#Using filter to check if the specific product is add to cart or not

@register.filter(name='currency')

def currency(number):
   return " Rs "+str(number)


@register.filter(name='multiply')

def multiply(number,number1):
   return number*number1



