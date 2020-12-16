from django.shortcuts import render
from home .models import Product

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
    context = {}
    return render(request, 'home/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'home/checkout.html', context)