from django.shortcuts import render, redirect
from shopping.models import Product, Price, Order
from django.contrib import messages
# Create your views here.

def index(request):
    context = {
        "products" : Product.objects.all()
    }
    return render(request, 'index.html', context)

def adminIndex(request):
    context = {
        "products" : Product.objects.all(),
        "price" : Price.objects.all()
    }

    return render(request, 'admin.html', context)

def addProduct(request):
    name = request.POST['product_name']
    code = request.POST['product_code']
    price = request.POST['price']
    new_product = Product.objects.create(product_name=name, product_code=code)
    new_price = Price.objects.create(original_price=price, product_id=new_product)

    return redirect('/store_admin')

def addPrice(request):
    errors = Price.objects.validator(request.POST)
    if len(errors):
        for key, val in messages.items():
            messages.error(request, val)
    
    else:
        price = request.POST['price']
        Price.objects.create(price=price)

    return redirect('/store_admin')

def orderProcess(request):
    q = request.POST['quantity']
    product_id = request.POST['product_id']
    product = Product.objects.get(product_code=product_id)
    price = product.price.original_price
    
    total_price = int(q)*float(price)
    print(total_price)

    new_order = Order.objects.create(quantity=q, total_price=total_price)

    return redirect('/order_complete/' + str(product_id))


def orderComplete(request, product_id):
    product = Product.objects.get(product_code=product_id)
    context = {
        "order" : Order.objects.last(),
        "product" : product
    }
    return render(request,'order_complete.html', context)

