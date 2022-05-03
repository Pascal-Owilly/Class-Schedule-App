from django.contrib import admin
from .models import Student, Tm, User
# Register your models here.

admin.site.register(User)
admin.site.register(Tm)
admin.site.register(Student)