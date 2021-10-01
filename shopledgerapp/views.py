from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ProductDetail, CustomerData, totalPrice
from .forms import dataEntry,productEntry
# Create your views here.

def index(request):
    product_detail = ProductDetail.objects.all()
    customer_detail = CustomerData.objects.all()
    total = totalPrice
    content = {
        'products':product_detail,
        'customer':customer_detail,
        'price':total,
    }

    return render(request,'shopledgerapp/index.html',content)

def createData(request):
    customer_form = dataEntry()
    if request.method == "POST":
        customer_form = dataEntry(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('index')
    content = {
        'form': customer_form
    }
    return render(request,'shopledgerapp/create.html',content)

def deleteData(request,pk):
    customer = CustomerData.objects.get(id = pk)
    if request.method == "POST":
        customer.delete()
        return redirect('index')
    return render(request,'shopledgerapp/delete.html',{"object":customer})

def editData(request,pk):
    customer = CustomerData.objects.get(id = pk)
    customer_form = dataEntry(instance=customer)
    if request.method == "POST":
        customer_form = dataEntry(request.POST,instance = customer)
        if customer_form.is_valid:
            customer_form.save()
            return redirect('index')
    return render(request,'shopledgerapp/create.html',{'form':customer_form})

def deleteAll(request):
    customer = CustomerData.objects.all()
    if request.method == "POST":
        customer.delete()
        return redirect('index')
    return render(request,'shopledgerapp/deleteall.html')

def createProduct(request):
    form = productEntry()
    if request.method == "POST":
        form = productEntry(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'shopledgerapp/createproduct.html',{'form':form})