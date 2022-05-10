from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Tm)
admin.site.register(Student)
admin.site.register(Announcements)
admin.site.register(Comments)
admin.site.register(Course)
admin.site.register(Attendance)
admin.site.register(Session)