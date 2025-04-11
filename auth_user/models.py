from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("The email is mandatory.")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True. ")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True. ")

        return self.create_user(email, password, **kwargs)
    

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, null=False, db_index=True)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    password = models.CharField(null=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.email