from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    modified = models.DateTimeField(auto_now=True)
    photo = models.ImageField(null=True, blank=True, upload_to='users')
    extract = RichTextField(null=True, blank=True)
    phone = models.CharField(null=True, blank=True, max_length=15)
    city = models.CharField(null=True, blank=True, max_length=255)
    country = models.CharField(null=True, blank=True, max_length=255)
    is_recruiter = models.BooleanField(default=False)