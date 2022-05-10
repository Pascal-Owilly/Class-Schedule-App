from django.contrib import admin
from.models import Course,Attendance, Student,Announcements, Comments,User

# Register your models here.
admin.site.register(Announcements)
admin.site.register(Comments)
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Attendance)
admin.site.register(Student)
# admin.site.register(Session)
