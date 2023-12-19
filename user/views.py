# from django.shortcuts import render
from django.views.generic.base import View
from .models import *
from django.shortcuts import render,redirect,get_object_or_404


# Create your views here.

class Index(View):
        def get(self, request, *args, **kwargs): 
            data = Customer.objects.all()
            context = {'data' : data}
            return render(request, 'index.html',context)
        
class AddCustomer(View):
    def get(self, request, *args, **kwargs): 
        return render(request, 'customer_form.html')
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        customer_number = request.POST.get('customer_number')
        meter_serial_number = request.POST.get('meter_serial_number')

        customer = Customer(name=name,contact=contact,address=address,customer_number=customer_number,meter_serial_number=meter_serial_number)
        customer.save()

        return redirect('index')
    

class EditCustomer(View):
    def get(self, request, customer_id, *args, **kwargs): 
        data =  get_object_or_404(Customer, customer_id=customer_id)
        context = {'data' : data}
        return render(request, 'editcustomer.html',context)
    
    def post(self, request,customer_id, *args, **kwargs):
        customer = get_object_or_404(Customer, customer_id=customer_id)
        customer.name = request.POST.get('name')
        customer.contact = request.POST.get('contact')
        customer.address = request.POST.get('address')
        customer.customer_number = request.POST.get('customer_number')
        customer.meter_serial_number = request.POST.get('meter_serial_number')

        customer.save()


        return redirect('index')
    

class ViewCustomer(View):
    def get(self, request, customer_id, *args, **kwargs): 
        data =  get_object_or_404(Customer, customer_id=customer_id)
        context = {'data' : data}
        return render(request, 'viewcustomer.html',context)
    

class DeleteCustomer(View):
    def get(self, request, customer_id, *args, **kwargs): 
        data =  get_object_or_404(Customer, customer_id=customer_id)
        data.delete()
        return redirect('index')

