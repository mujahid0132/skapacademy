from django.db import models
from django_quill.fields import QuillField
class Blog(models.Model):
    title = models.CharField(max_length=50 ,default="")
    image = models.ImageField(upload_to="blogs/",default="/blogs/default/default.png")
    description = QuillField()
    is_archived = models.BooleanField(default=False) 
    def __str__(self):
        return str(self.title) 
