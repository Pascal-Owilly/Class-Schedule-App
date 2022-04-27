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

class Course(models.Model):
 course_name = models.CharField(max_length=500)
 date_created = models.DateField()
 date_updated = models.DateField()
 Student = models.ForeignKey(User,on_delete = models.CASCADE)

 def save_course(self):
  self.save()

 def delete_course(self):
  self.delete()