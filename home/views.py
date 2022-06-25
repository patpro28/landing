from django.shortcuts import render
from django.views.generic import TemplateView

from home.models import Landing

# Create your views here.

class Home(TemplateView):
  template_name: str = 'home.html'

  def get_context_data(self, **kwargs):
    landing = Landing.objects.all().order_by('-priority').first()
    context = super().get_context_data(**kwargs)
    context['description'] = landing.about
    context['title'] = landing.title
    return context