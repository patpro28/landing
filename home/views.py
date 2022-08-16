from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Landing, Logo, Narbar, HomeBanner, About, Reason, Teacher,Student, Class, Feedback

# Create your views here.

class Home(TemplateView):
  template_name: str = 'home.html'

  def get_context_data(self, **kwargs):
    landing = Landing.objects.all().order_by('-priority').first()
    logo = Logo.objects.all()
    navbar = Narbar.objects.all()
    homebanner = HomeBanner.objects.all()
    about = About.objects.all()
    reason = Reason.objects.all()
    teacher = Teacher.objects.all()
    student = Student.objects.all()
    classes = Class.objects.all()
    feedback = Feedback.objects.all()


  


    
    
    context = super().get_context_data(**kwargs)
 
   

    context['logo_section'] = logo
    context['navbar_section'] = navbar
    context['banner_section'] = homebanner
    context['about_section'] = about
    context['reason_section'] = reason
    context['teacher_section'] = teacher
    context['student_section'] = student
    context['class_section'] = classes
    context['feedback_section'] = feedback






   

    return context