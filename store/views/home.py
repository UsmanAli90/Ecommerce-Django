from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Categorie
from django.views import View

# Create your views here.

class Index(View):
    def post(self,request):
        #this will get us the product ID to add to cart
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
               if remove:
                  if quantity<=1:
                     cart.pop(product)
                  else:
                    cart[product]=quantity-1
               else:
                  cart[product]=quantity+1
            else:
               cart[product]=1
        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart
        print('Cart is :', request.session['cart'])
        # print(product)
        return redirect('homepage')

    def get(self,request):
         cart=request.session.get('cart')
         if not cart:
            request.session['cart']={}
         prds=None
        #  request.session.get('cart').clear()
         category=Categorie.get_all_categories()
         categoryID=request.GET.get('category')
         if(categoryID):
          prds=Product.get_all_products_by_id(categoryID)
         else:
          prds=Product.get_all_products()
    # return render(request,'index.html')
         data={}
         data['products']=prds
         data['categories']=category
         print('you are' ,request.session.get('email'))
         return render(request,'index.html',data)



