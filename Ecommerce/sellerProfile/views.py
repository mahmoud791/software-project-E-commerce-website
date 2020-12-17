from django.shortcuts import render , redirect
from django.http import HttpResponse
from home.models import Product
# Create your views here.

def sellerProfile (request):
    return render(request,"sellerprofile/sellerprofile.html")


def addNewProduct (request):

    name=request.POST["name"]
    price=request.POST["price"]
<<<<<<< Updated upstream
    category=request.POST["category"]
    description=request.POST["description"]
    image=request.FILES["image"]
    newproduct = Product(name=name,description=description,price=price,image=image, category= category)
    newproduct.save()
    
=======
    
    category=request.POST["category"]
    description=request.POST["description"]
    image=request.FILES["image"]

    newproduct = Product(name=name,description=description,price=price,image=image, category= category)

    newproduct.save()
>>>>>>> Stashed changes
    return redirect("/sellerprofile")
