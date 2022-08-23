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


class Logo(models.Model):
  logo = models.CharField(_("link"), max_length=1024)

  def __str__(self) -> str:
      return self.logo

class Setting(models.Model):
  theme_color = models.CharField(_("Theme Color"), max_length=1024, blank=True)
  text_color = models.CharField(_("Text Color"), max_length=1024, blank=True)

  def __str__(self) -> str:
      return self.theme_color


class Narbar(models.Model):
  section = models.CharField(_("Name"), max_length=1024)
  id_section = models.CharField(_("ID"), max_length=1024)
  link = models.CharField(_("link"), max_length=1024)

  def __str__(self) -> str:
      return self.section

class HomeBanner(models.Model):
  bg_link = models.CharField(_("Background Link"), max_length=1024)

  def __str__(self) -> str:
      return self.bg_link

class About(models.Model):
  img_1 = models.CharField(_("Image 1"), max_length=1024)
  img_2 = models.CharField(_("Image 2"), max_length=1024)
  title = models.CharField(_("Title"), max_length=1024)
  content = models.CharField(_("Content"), max_length=1024)

  def __str__(self) -> str:
      return self.title

class Reason(models.Model):
  title = models.CharField(_("Title"), max_length=1024)
  content = models.CharField(_("Content"), max_length=1024)
  bg = models.CharField(_("Image"), max_length=1024, blank=True)

  def __str__(self) -> str:
      return self.title


class Teacher(models.Model):
  img = models.CharField(_("Image"), max_length=1024)
  name = models.CharField(_("Name"), max_length=1024)
  content = models.TextField(_("Content"), max_length=1024, blank=True)

  def __str__(self) -> str:
      return self.name

class Student(models.Model):
  img = models.CharField(_("Image"), max_length=1024)
  name = models.CharField(_("Name"), max_length=1024)
  content = models.CharField(_("Content"), max_length=1024, blank=True)

  def __str__(self) -> str:
      return self.name



class Feedback(models.Model):
  name = models.CharField(_("Name"), max_length=1024)
  infor = models.CharField(_("Information"), max_length=1024, blank=True)
  img = models.CharField(_("Image"), max_length=1024, blank=True)
  feedback = models.CharField(_("Feedback"), max_length=1024, blank=True)
  time = models.CharField(_("Time"), max_length=1024, blank=True)


  def __str__(self) -> str:
      return self.name


class Class(models.Model): 

  class_name = models.CharField(max_length=200, null=True) 
 
  
  def __str__(self) -> str:
      return self.class_name

class Room(models.Model): 
  room_parent = models.ForeignKey(Class,related_name='addition',on_delete=models.CASCADE) 
  name = models.CharField(_("Name"), max_length=1024, blank=True)
  student = models.CharField(_("Student"), max_length=1024, blank=True)
  teacher = models.CharField(_("Teacher"), max_length=1024, blank=True)
  time = models.CharField(_("Time"), max_length=1024, blank=True)

  def __str__(self) -> str:
      return self.name


class Contact(models.Model): 
  name = models.CharField(_("Name"), max_length=1024, blank=True)
  img = models.CharField(_("Image"), max_length=1024, blank=True)
  link = models.CharField(_("Link"), max_length=1024, blank=True)

  def __str__(self) -> str:
      return self.name 

  






