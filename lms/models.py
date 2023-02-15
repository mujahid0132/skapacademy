from django.db import models


# Create your models here.
class LmsCourse(models.Model):
    name = models.CharField(max_length=50,default='',unique=True)
    def __str__(self):
        return str(self.name) 
class LmsRequest(models.Model):
    name = models.CharField(max_length=50,default='',unique=True)
    email = models.EmailField(max_length=254,default='')
    phone_number = models.CharField(max_length=13,default='',unique=True)
    course_name = models.ForeignKey(LmsCourse,on_delete=models.CASCADE)
    message = models.TextField(null = True)
    date_requested = models.DateTimeField(auto_now_add=True)
    # def clean(self):
    #     if self.price or self.discounted_price is not None:
    #         if self.discounted_price>self.price:
    #             raise ValidationError('Discounted-Price Should Be Less Than Price')
    # def save(self, *args, **kwargs):
        # if self.discounted_price>self.price:
        #     messages.error("you can not add discouted price more than price")
        # self.slug = self.name.replace(" ", "-")
        # super().save(*args, **kwargs)
    # def delete(self, *args, **kwargs):
    #     ProductArchive.objects.create(
    #         name = self.name,
    #         image = self.image,
    #         description = self.description,
    #         type = self.type,
    #         price = self.price,
    #         discounted_price = self.discounted_price,
    #         slug = self.slug,
    #         popularity = self.popularity
    #         )
    #     super().delete(*args, **kwargs)
    def __str__(self):
        return str(self.name) 