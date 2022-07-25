from msilib.schema import Class
from django.contrib import admin
from .models import HomeButton, HomeContent, Landing, Navigation, About, Achievement, Classroom, HomeButton, Emath
# Register your models here.

admin.site.register(Landing)
admin.site.register(Navigation)
admin.site.register(HomeContent)
admin.site.register(HomeButton)
admin.site.register(About)
admin.site.register(Achievement)
admin.site.register(Classroom)
admin.site.register(Emath)



