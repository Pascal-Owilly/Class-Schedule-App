from django.db import models
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


from cloudinary.models import CloudinaryField
# Create your models here.
class Profile(models.Model):
  user = models.ForeignKey(User,on_delete = models.CASCADE)
  is_tm=models.BooleanField(default=False)
  is_student=models.BooleanField(default=True)
  
  
  def __str__(self):
        return str(self.user.username)





  def save_profile(self):
    self.save()

  def delete_profile(self): 
    self.delete()

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Course(models.Model):
 course_name = models.CharField(max_length=500)
 date_created = models.DateField()
 date_updated = models.DateField()
 
 def __str__(self):
    return self.course_name

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
    return self.title

  
  def save_announcements(self):
    self.save()


class Comments(models.Model):
  announcement = models.ForeignKey(Announcements, related_name='comments', on_delete=models.CASCADE)
  comment = models.TextField()
  user = models.ForeignKey(User,on_delete = models.CASCADE)
  date_posted = models.DateTimeField( auto_now_add = True)

  def __str__(self):
    return self.comment

  def save_comment(self):
    self.save()

class Student(models.Model):
 user = models.ForeignKey(User,related_name="student",on_delete = models.CASCADE)
 course = models.ForeignKey(Course,on_delete = models.CASCADE)

 def __str__(self):
        return str(self.user.username)



 def save_student(self):
    self.save()
    
 def delete_student(self):
    self.delete()

class Session(models.Model):
  name = models.CharField(max_length=255)
  time = models.DateTimeField()
  link = models.URLField()
  attendees = models.ManyToManyField(User, related_name="user")
  posted_by = models.ForeignKey(User,on_delete = models.CASCADE, default=None)

class Attendance(models.Model):
  attendance =  models.IntegerField()
  student = models.ForeignKey(Student,on_delete = models.CASCADE)

  def save_attendance(self):
   self.save()


class Tm(models.Model):
    user=models.OneToOneField(User, related_name="tm", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)


