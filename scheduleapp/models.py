from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField
# Create your models here.
class Profile(models.Model):
 user = models.OneToOneField(User,on_delete = models.CASCADE)
 profile_pic = CloudinaryField('image')
 role = models.CharField(max_length=20)
 

 def save_profile(self):
  self.save()

 def delete_profile(self): 
  self.delete()


 def save_student(self):
  self.save()

 def delete_student(self): 
  self.delete()
  
def __str__(self):
        return self.username


class Course(models.Model):
 course_name = models.CharField(max_length=500)
 date_created = models.DateField()
 date_updated = models.DateField()


 def save_course(self):
  self.save()

 def delete_course(self):
  self.delete()

class Student(models.Model):
 student = models.ForeignKey(User,on_delete = models.CASCADE)
 course = models.ForeignKey(Course,on_delete = models.CASCADE)


 def save_student(self):
  self.save()

 def delete_student(self):
  self.delete()

class Attendance(models.Model):
  attendance =  models.IntegerField()
  student = models.ForeignKey(Student,on_delete = models.CASCADE)

  def save_attendance(self):
   self.save()