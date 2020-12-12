from django.shortcuts import render

items = [
    {
        "image":"https://assets.crowdspring.com/marketing/landing-page/crowdspring-product-design-phase1-1120.jpg",
        "price":"30$",
        "description":"simple crystal vase",
        "name":"vase",
        "reviews":3
    },
    {
        "image":"https://assets.crowdspring.com/marketing/landing-page/crowdspring-product-design-phase1-1120.jpg",
        "price":"30$",
        "description":"simple crystal vase",
        "name":"vase",
        "reviews":3
    },
    {
        "image":"https://assets.crowdspring.com/marketing/landing-page/crowdspring-product-design-phase1-1120.jpg",
        "price":"30$",
        "description":"simple crystal vase",
        "name":"vase",
        "reviews":3
    },
    {
        "image":"https://assets.crowdspring.com/marketing/landing-page/crowdspring-product-design-phase1-1120.jpg",
        "price":"30$",
        "description":"simple crystal vase",
        "name":"vase",
        "reviews":3
    },
    {
        "image":"https://assets.crowdspring.com/marketing/landing-page/crowdspring-product-design-phase1-1120.jpg",
        "price":"30$",
        "description":"simple crystal vase",
        "name":"vase",
        "reviews":3
    },
    {
        "image":"https://assets.crowdspring.com/marketing/landing-page/crowdspring-product-design-phase1-1120.jpg",
        "price":"30$",
        "description":"simple crystal vase",
        "name":"vase",
        "reviews":3
    },
    {
        "image":"https://assets.crowdspring.com/marketing/landing-page/crowdspring-product-design-phase1-1120.jpg",
        "price":"30$",
        "description":"simple crystal vase",
        "name":"vase",
        "reviews":3
    },
    {
        "image":"https://assets.crowdspring.com/marketing/landing-page/crowdspring-product-design-phase1-1120.jpg",
        "price":"30$",
        "description":"simple crystal vase",
        "name":"vase",
        "reviews":3
    },
    {
        "image":"https://assets.crowdspring.com/marketing/landing-page/crowdspring-product-design-phase1-1120.jpg",
        "price":"30$",
        "description":"simple crystal vase",
        "name":"vase",
        "reviews":3
    },
    {
        "image":"https://assets.crowdspring.com/marketing/landing-page/crowdspring-product-design-phase1-1120.jpg",
        "price":"30$",
        "description":"simple crystal vase",
        "name":"vase",
        "reviews":3
    },


   

]

def homePage(request):
    context = {
        "items":items
    }

    return render(request,'home/homePage.html',context)