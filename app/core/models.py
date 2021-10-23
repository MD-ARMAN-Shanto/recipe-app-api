from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_kwargs):
        """creates and saves a new user"""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """creating and saving a new super user"""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """custom user model that supports email instead of username"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
