from django.db import models
from .category import Categorie

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    #Adding a foreign key of categories into products
    category=models.ForeignKey(Categorie,on_delete=models.CASCADE, default=1)
    description=models.CharField(max_length=200,default='',null='true',blank='True')
    image=models.ImageField(upload_to="uploads/products/")



#this function will return us all the products
    @staticmethod

    def get_all_products():
        return Product.objects.all()
   
   
    @staticmethod

    def get_all_products_by_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_product()

    @staticmethod

    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
