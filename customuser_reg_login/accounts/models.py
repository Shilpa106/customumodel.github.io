from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _


class CompanyCustomUser(AbstractUser):
    
    name = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(verbose_name="email",max_length=60,unique=True)
    username = models.CharField(max_length=30,unique=True)
    website = models.CharField(max_length=50,null=True,blank=True)
    phone=models.CharField(max_length=14,null=True,blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True,blank=True)
    country = models.CharField(max_length=50, null=True,blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

   