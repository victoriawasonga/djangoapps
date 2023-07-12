from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)

class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if username is None:
            raise TypeError("Username cannot be empty")
        if email is None:
            raise TypeError('Email field must not be null')
        user=self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save()
    

    def create_superuser(self,username,email,password):
        if password is None:
            raise TypeError("Username cannot be empty")
        user=self.model(username=username,email=self.normalize_email(email))
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user
    
class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=255, unique=True,db_index=True)
    email=models.EmailField(max_length=255, unique=True,db_index=True)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    objects=UserManager()

    def __str__(self):
        return self.email
    
    def tokens(self):
        return ''
    