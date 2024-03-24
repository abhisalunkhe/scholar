from django.db import models

# Create your models here.
class ContactModule(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    message = models.TextField()

class CoursesModule(models.Model):
    className = models.CharField(max_length = 20)
    poster = models.ImageField(upload_to='courses')
    category = models.CharField(max_length = 20)
    price = models.IntegerField()
    instructor = models.CharField(max_length = 50)
    heading = models.CharField(max_length = 35)

class ScheduleModule(models.Model):
    isdone = models.BooleanField(default = False)
    poster = models.ImageField(upload_to='events')
    category = models.CharField(max_length = 20)
    heading = models.CharField(max_length = 35)
    date = models.TextField()
    duration = models.TextField()
    price = models.IntegerField()

class TeamDeatilsModule(models.Model):
    selfie = models.ImageField(upload_to='team')
    category = models.CharField(max_length = 30)
    name = models.CharField(max_length = 30)
    facebook = models.TextField()
    twitter = models.TextField()
    linkedin = models.TextField()

class TestimonialModule(models.Model):
    isvisible = models.BooleanField(default = True)
    selfie = models.ImageField(upload_to="testimonial")
    description = models.TextField()
    category = models.CharField(max_length = 30)
    name = models.CharField(max_length = 30)