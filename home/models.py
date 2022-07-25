from django.db import models
from django.utils.translation import gettext_lazy as _
from martor.models import MartorField

# Create your models here.

class Landing(models.Model):
  about = MartorField(_("description"), blank=False)
  priority = models.IntegerField(_("priority"), default=0)
  title = models.CharField(_("title"), max_length=255, null=True)

  def __str__(self) -> str:
    return self.title


class Navigation(models.Model):
  name = models.CharField(_("name"), max_length=50)
  link = models.CharField(_("link"), max_length=255)

  def __str__(self) -> str:
    return self.name

class HomeContent(models.Model):
  title = models.CharField(_("content1"), max_length=255, blank=True)
  title2 = models.CharField(_("content2"), max_length=255, blank=True)
  title3 = models.CharField(_("content3"), max_length=255, blank=True)
  title4 = models.CharField(_("content4"), max_length=255, blank=True)
  title5 = models.CharField(_("content5"), max_length=255, blank=True)

  def __str__(self) -> str:
    return self.title

class HomeButton(models.Model):
  button = models.CharField(_("name button"), max_length=255, blank=True)
  link = models.CharField(_("link"), max_length=255, blank=True)
  
  def __str__(self) -> str:
    return self.button

class HomeImg(models.Model):
  link = models.CharField(_("link img"), max_length=255, blank=True)
  img_1 = models.CharField(_("img1"), max_length=255, blank=True)
  img_1 = models.CharField(_("img1"), max_length=255, blank=True)
  img_1 = models.CharField(_("img1"), max_length=255, blank=True)


  def __str__(self) -> str:
    return self.button

class About(models.Model):
  title = models.CharField(_("title"), max_length=255, blank=True)
  content = models.CharField(_("content"), max_length=255, blank=True)
  img_link = models.CharField(_("link"), max_length=255, blank=True)

  def __str__(self) -> str:
    return self.title

class Achievement(models.Model):
  number = models.CharField(_("number"), max_length=255, blank=True)
  content = models.CharField(_("content"), max_length=255, blank=True)

  def __str__(self) -> str:
    return self.number

class Class(models.Model):
  name = models.CharField(_("name"), max_length=255, blank=True)
  title = models.CharField(_("title"), max_length=255, blank=True)
  note = models.CharField(_("note"), max_length=255, blank=True)
  link = models.CharField(_("link"), max_length=255, blank=True)

  def __str__(self) -> str:
    return self.name

class Classroom (models.Model):
  name = models.CharField(_("name"), max_length=255, blank=True)
  title = models.CharField(_("title"), max_length=255, blank=True)
  note = models.CharField(_("note"), max_length=255, blank=True)
  link = models.CharField(_("link"), max_length=255, blank=True)

  def __str__(self) -> str:
    return self.name

class Emath (models.Model):
  title = models.CharField(_("tile"), max_length=255, blank=True)
  content = models.CharField(_("content"), max_length=255, blank=True)
  note = models.CharField(_("note"), max_length=255, blank=True)
  link = models.CharField(_("link"), max_length=255, blank=True)
  appstore = models.CharField(_("appstore_link"), max_length=255, blank=True)
  chplay = models.CharField(_("chplay_link"), max_length=255, blank=True)


  def __str__(self) -> str:
    return self.title