from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

items = Product.objects.all()

def homePage(request):
    context = {
        "items":items
    }

    return render(request,'home/homePage.html',context)


def user_profile(request):
    context = {}
    return render(request, 'profile/profile.html', context)

def category(request,category):
    items = {}
    if category =='clothes':
        items = Product.objects.filter(category='clothes')
    elif category=='shoes':
        items = Product.objects.filter(category='shoes')
    elif category=='watches':
        items = Product.objects.filter(category='watches')
    elif category=='laptops':
        items = Product.objects.filter(category='laptops')
    elif category=='mobile_phones':
        items = Product.objects.filter(category='mobile phones')
    elif category=='headphones&headsets':
        items = Product.objects.filter(category='headphones/headsets')
    elif category=='perfumes&deodrants':
        items = Product.objects.filter(category='perfumes/deodrants')
    elif category=='accessories':
        items = Product.objects.filter(category='accessories')
    elif category=='kid_toys':
        items = Product.objects.filter(category='kid toys')


    context = {
        'items':items
    }
    

    return render(request,'category/category.html',context)



def cart(request):

    if request.user.is_authenticated:
        customer=request.user.customer
        order, created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
    
    context = {'items':items,'order':order}
    return render(request, 'home/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'home/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print('Action: ',action)
    print('productId: ',productId)

    customer= request.user.customer
    product=Product.objects.get(id=productId)
    order, created=Order.objects.get_or_create(customer=customer,complete=False)
    orderItem ,created=OrderItem.objects.get_or_create(order=order,product=product)
    if action=='add':
        orderItem.quantity=(orderItem.quantity+1)
    elif action=='remove':
        orderItem.quantity=(orderItem.quantity-1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('Item was added', safe=False)