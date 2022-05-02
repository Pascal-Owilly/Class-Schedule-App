from django.contrib import admin
from.models import Profile,Course,Attendance, Session, Student,Announcements, Comments

# Register your models here.
admin.site.register(Announcements)
admin.site.register(Comments)
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Attendance)
admin.site.register(Student)
admin.site.register(Session)
