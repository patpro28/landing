from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Landing, Navigation, Logo, HomeContent, About, Achievement, Classroom, HomeButton, New, CoppyRight

# Create your views here.

class Home(TemplateView):
  template_name: str = 'home.html'

  def get_context_data(self, **kwargs):
    landing = Landing.objects.all().order_by('-priority').first()
    navbar = Navigation.objects.all()
    logo = Logo.objects.all()
    home_content = HomeContent.objects.all()
    about = About.objects.all()
    achievement = Achievement.objects.all()
    classes = Classroom.objects.all()
    buttons = HomeButton.objects.all()
    new = New.objects.all()
    coppyright = CoppyRight.objects.all()


    
    
    context = super().get_context_data(**kwargs)
    context['description'] = landing.about
    context['title'] = landing.title
    context['nav'] = navbar
    context['logo_section'] = logo
    context['home_info'] = home_content
    context['buttons_section'] = buttons
    context['about_section'] = about
    context['achievement_section'] = achievement
    context['classes_section'] = classes
    context['new_section'] = new
    context['coppyright_section'] = coppyright

    return context