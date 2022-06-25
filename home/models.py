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