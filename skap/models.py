from django.db import models
from django_quill.fields import QuillField
from django.utils.text import slugify
class Blog(models.Model):
    title = models.CharField(max_length=50 ,default="")
    image = models.ImageField(upload_to="blogs/",default="/blogs/default/default.png")
    description = QuillField()
    is_archived = models.BooleanField(default=False) 
    date_posted = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
class Contact(models.Model):
    name = models.CharField(max_length=50 ,default="")
    email = models.EmailField( max_length=254)
    phone_no = models.CharField(max_length=17)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name) 
    
class Testimonial(models.Model):
    name = models.CharField(max_length=50 ,default="")
    image = models.ImageField(upload_to="testimonial/",default="/blogs/default/default.png")
    designation = models.CharField(max_length=50 ,default="")
    comments = models.TextField(max_length=400)
    def __str__(self):
        return str(self.name) 
    

