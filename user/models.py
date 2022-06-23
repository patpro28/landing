from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

# Create your models here.


class ProfileManager(BaseUserManager):

    def create_user(self, username, fullname, password=None):
        if not username:
            raise ValueError('Username cant empty!')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, fullname, password=None):
        if not username:
            raise ValueError('Username cant empty!')
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Profile(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(_("Username"), max_length=30, unique=True)
  email = models.EmailField(_("Email"), max_length=254, blank=True)
  is_staff = models.BooleanField(_("is staff"), default=False)
  is_active = models.BooleanField(_("Active"), default=True)

  objects = ProfileManager()

  USERNAME_FIELD = 'username'

  def __str__(self) -> str:
    return self.username

  class Meta:
    ordering = ['username']