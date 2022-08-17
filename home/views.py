from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Landing, Setting, Logo, Narbar, HomeBanner, About, Reason, Teacher,Student, Class01, Class02, Class03, Feedback

# Create your views here.

class Home(TemplateView):
  template_name: str = 'home.html'

  def get_context_data(self, **kwargs):
    landing = Landing.objects.all().order_by('-priority').first()
    logo = Logo.objects.all()
    setting = Setting.objects.all()
    navbar = Narbar.objects.all()
    homebanner = HomeBanner.objects.all()
    about = About.objects.all()
    reason = Reason.objects.all()
    teacher = Teacher.objects.all()
    student = Student.objects.all()
    classes01 = Class01.objects.all()
    classes02 = Class02.objects.all()
    classes03 = Class03.objects.all()
    feedback = Feedback.objects.all()


  


    
    
    context = super().get_context_data(**kwargs)
 
   

    context['logo_section'] = logo
    context['setting_section'] = setting
    context['navbar_section'] = navbar
    context['banner_section'] = homebanner
    context['about_section'] = about
    context['reason_section'] = reason
    context['teacher_section'] = teacher
    context['student_section'] = student
    context['class_01_section'] = classes01
    context['class_02_section'] = classes02
    context['class_03_section'] = classes03
    context['feedback_section'] = feedback


    print(setting)





   

    return context