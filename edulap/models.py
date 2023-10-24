from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    discription = models.TextField()
    
    def __str__(self):
        return self.name

class Customer(models.Model):
    USER_CHOICES = [
        ('teacher' , 'teacher'),
        ('student' , 'student')
    ]
    userName = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=USER_CHOICES)
    userMail = models.EmailField(unique=True)
    userPhone = models.IntegerField()
    
    def __str__(self):
        return str(self.userName)


class Meeting(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True)
    meetingName = models.CharField(max_length=50)
    meetingPrice = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    slug = models.SlugField(default="", blank= True, null= True, max_length=255)
    startDate = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.meetingName)
        super(Meeting, self).save(*args, **kwargs)  

    def __str__(self):
        return self.meetingName
    
class Courses(models.Model) :
    name = models.CharField(max_length= 50)
    coursePrice = models.DecimalField(max_digits = 5,decimal_places = 2)
    courseRate = models.IntegerField(default=0,validators=[MinValueValidator(0),
                                  MaxValueValidator(5)])
    courseDescription = models.TextField(blank= True, null= True)
    start_at = models.DateTimeField(auto_created=True)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    slug = models.SlugField(default='', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Courses, self).save(*args, **kwargs)  

    def __str__(self):
        return self.name