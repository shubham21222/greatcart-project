<<<<<<< HEAD
from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_avaliable=True)

    context = {
        'products':products,
    }



=======
from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_avaliable=True)

    context = {
        'products':products,
    }



>>>>>>> 1baa7bd3e80870e161f11c7e57ef726649ae0d87
    return render(request,'home.html',context)