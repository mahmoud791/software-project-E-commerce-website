from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=64,null=True)
      
    def __str__(self):
        return self.name
    
    

             

class Product (models.Model):
    CATEGORY=(
        ('clothes','clothes'),
        ('shoes','shoes'),
        ('watches','watches'),
        ('laptops','laptops'),
        ('mobile phones','mobile phones'),
        ('headphones/headsets','headphones/headsets'),
        ('perfumes/deodrants','perfumes/deodrants'),
        ('accessories','accessories'),
        ('kid toys','kid toys'),


    )


    name = models.CharField(max_length=200,null=True)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(null=True,blank=True)
    category = models.CharField(max_length=64,choices=CATEGORY,null=True)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    customer = models.ForeignKey(Customer,null=True,on_delete = models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.transaction_id)

    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    order = models.ForeignKey(Order,null=True,blank=True,on_delete = models.SET_NULL)
    product = models.ForeignKey(Product,null=True,blank=True,on_delete = models.SET_NULL)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    @property
    def get_total(self):
        total=self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,null=True,on_delete = models.SET_NULL)
    order = models.ForeignKey(Order,null=True,blank=True,on_delete = models.SET_NULL)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    zipcode = models.CharField(max_length=200,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address





