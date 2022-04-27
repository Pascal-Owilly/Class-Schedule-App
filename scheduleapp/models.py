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


class Announcements(models.Model):
  title = models.CharField(max_length= 500)
  message = models.TextField()
  user = models.ForeignKey(User,on_delete = models.CASCADE)
  date_created= models.DateTimeField(auto_now_add=True)
  date_updated= models.DateTimeField( auto_now = True)

  def __str__(self):
    self.title 

  def save_announcements(self):
    self.save()


class Comments(models.Model):
  announcement = models.ForeignKey(Announcements, related_name='comments', on_delete=models.CASCADE)
  comment = models.TextField()
  name = models.ForeignKey(User,on_delete = models.CASCADE)
  date_posted = models.DateTimeField( auto_now_add = True)

  def __str__(self):
    return self.comment

  def save_comment(self):
    self.save()


class Session(models.Model):
  name = models.CharField(max_length=255)
  time = models.DateTimeField()
  link = models.URLField()
  attendees = models.ManyToManyField(User, related_name="user")
  posted_by = models.ForeignKey(User,on_delete = models.CASCADE, default=None)









