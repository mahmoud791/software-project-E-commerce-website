from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.

class user(models.Model):
    user_name = models.CharField(max_length = 64)
    password = models.CharField(max_length = 64)
    email = models.CharField(max_length = 64)



class profile(models.Model):
    #This line will ensure only one instance of this model can be created for each User.
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    #OneToOne relation means that for each user a single profile will be created
    # i.e. there can't be 2 profiles for the same user and there can't be a user with no profile.

    #Other values for user:
    is_seller = models.BooleanField(default = True)

#post_save to make django create/update a profile each time a user is created/updated.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)
    
# @reciever is a decorator that take a "signal (to the db)" as an arguement and acts on a function whenever the signal is triggered. 
#lw bygeelak error mn el class dah excute the following command
#pip install pylint-django
#then in VSCode file > prefrences> settings> extentions > find python > find Linting: Pylint Path and change pylint to pylint_django
@receiver(post_save, sender=User)
def save_proile(sender, instance, **keywargs):
    instance.profile.save()