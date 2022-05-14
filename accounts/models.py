from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from rest_framework.authtoken.models import Token
from accounts.manager import MyAccountsManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# from django.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=80, unique=True)
    username = models.CharField(max_length=100, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.DateField(default=datetime.today)
    bio = models.TextField(blank=True, null=True, max_length=2000)
    profile_pic = models.ImageField(upload_to='profile_pic/', blank=True, null=True)

    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'age']

    # objects = MyAccountsManager

    # def __str__(self):
    #     return self.username + " " + self.email

    # def has_perm(self, perm, obj=None):
    #     return self.is_admin

    # def has_module_perm(self, app_label):
    #     return True

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    


# for user in settings.AUTH_USER_MODEL:
#     Token.objects.get_or_create(user=user)