from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View




class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        postdata=request.POST
        first_name=postdata.get('firstname')
        last_name=postdata.get('lastname')
        email=postdata.get('email')
        phone=postdata.get('phone')
        password=postdata.get('password')

        value={
            'first_name':first_name,
            'last_name':last_name,
            'phone':phone,
            'email':email
        }

        customer=Customer(first_name=first_name,last_name=last_name,email=email,phone=phone,password=password)
        # validations
        error_message=self.validateCustomer(customer)
    
        #saving
        if not error_message:
            #to hash password
            customer.password=make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data={
                'error':error_message,
                'values':value
            }

            return render(request,'signup.html',data)
    
    def validateCustomer(self,customer):
        error_message=None
        if(not customer.first_name):
            error_message="First name Required"
        elif len(customer.first_name)<3:
            error_message="First Name must be 3 characters long"
        elif(not customer.last_name):
            error_message="Last name Required"
        elif len(customer.last_name)<3:
            error_message="Last Name must be 3 characters long"
        elif(not customer.phone):
            error_message="Phone Number Required"
        elif len(customer.phone)<10:
            error_message="Phone Number must be 10 characters long"
        elif(not customer.email):
            error_message="Email Required"
        elif len(customer.password)<6:
            error_message="Password must be more then 6 characters"
        elif customer.isExist():
                error_message="Email Address already registered"
        return error_message
