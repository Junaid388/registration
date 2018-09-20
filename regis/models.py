from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


#CHOICES = (('Developer','Developer'),('Reporter', 'Reporter'),('Manager','Manager'),)

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Email_Address = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '9848012345'. Up to 10 digits allowed.")
    Phone_Number = models.CharField(validators=[phone_regex], max_length=10, blank=True) # validators should be a list
    #Contact_Number= models.CharField(max_length=10)
    #Category= models.CharField(max_length=20, choices=CHOICES, default='Developer')
    Password = models.CharField(max_length=10)
    Confirm_Password = models.CharField(max_length=10)

    def publish(self):
        self.save()

    def __str__(self):
        return self.First_Name
    @property
    def friendly_email(self):
        return mark_safe(u"%s <%s>") % (escape(self.fullname), escape(self.Email_Address))
