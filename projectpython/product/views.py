from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from product.models import Product


def  index(request):
    return render(request, 'productpage/index.html')


def addproduct(request):
    errors = Product.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    products = Product.objects.create(product_name=request.POST['product_name'],
                                      product_weight=request.POST['product_weight'],
                                      product_price=request.POST['product_price'])
    products.save()
    request.session['id'] = products.id
    return redirect('/productsuccess')


# Create your views here.

def productsuccess(request):
    products = Product.objects.get(id=request.session['id'])
    context = {
        "products": products
    }
    return render(request, 'productpage/productsuccess.html', context)
