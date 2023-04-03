from django.db import models


# Create your models here.
class LmsCourse(models.Model):
    name = models.CharField(max_length=50,default='',unique=True)
    is_archived = models.BooleanField(default=False) 
    def __str__(self):
        return str(self.name) 
class LmsRequest(models.Model):
    name = models.CharField(max_length=50,default='',unique=True)
    email = models.EmailField(max_length=254,default='')
    phone_number = models.CharField(max_length=13,default='',unique=True)
    course_name = models.ForeignKey(LmsCourse,on_delete=models.CASCADE)
    message = models.TextField(null = True)
    date_requested = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False) 
    def __str__(self):
        return str(self.name) 