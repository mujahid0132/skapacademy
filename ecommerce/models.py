from django.db import models
from django.core.exceptions import ValidationError
from django_quill.fields import QuillField
from mptt.models import MPTTModel

class ProductType(MPTTModel):
    name = models.CharField(max_length=255,primary_key=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=50,default='',unique=True)
    sku = models.CharField(max_length=50,default='')
    image = models.ImageField(upload_to="products/",default="/products/default/default.png")
    description = QuillField()
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=0)
    slug = models.SlugField(max_length=255,unique=True,blank=True)
    popularity = models.IntegerField(default=0)
    def clean(self):
        if self.price or self.discounted_price is not None:
            if self.discounted_price>self.price:
                raise ValidationError('Discounted-Price Should Be Less Than Price')
    def save(self, *args, **kwargs):
        self.slug = self.name.replace(" ", "-")
        super().save(*args, **kwargs)
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
class Order(models.Model):
    first_name = models.CharField(max_length=50,default='')
    last_name = models.CharField(max_length=50,default='')
    email = models.CharField(max_length=50,default='')
    phone_no = models.CharField(max_length=50,default='')
    address = models.CharField(max_length=50,default='')
    city = models.CharField(max_length=50,default='')
    country = models.CharField(max_length=50,default='')
    postal_code = models.CharField(max_length=50,default='')
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100)
    total_price = models.IntegerField(default=0)
    is_archived = models.BooleanField(default=False)
    def archive(self):
        self.is_archived = True
        self.save()
    def unarchive(self):
        self.is_archived = False
        self.save()        
    def ret(self):
        return self.first_name
    def save(self, *args, **kwargs):
        print(self.ret())

        super().save(*args, **kwargs)
    # def delete(self, *args, **kwargs):
    #     ProductArchive.objects.create(
    #         first_name = self.first_name,
    #         last_name = self.last_name,
    #         email_or_phone_no = self.email_or_phone_no,
    #         address = self.address,
    #         city = self.city,
    #         country = self.country,
    #         postal_code = self.postal_code,
    #         date_ordered = self.date_ordered,
    #         complete = self.complete,
    #         transaction_id = self.transaction_id,
    #         total_price = self.total_price,
    #         )
    #     super().delete(*args, **kwargs)
    def __str__(self):
        return str(self.first_name)

# @receiver(pre_save, sender=Order)
# def update_order_items(sender, instance, **kwargs):
#     order = instance
#     order_item = OrderItem.objects.filter(order=order)
#     for i in range(order_item.__len__()):
#         product = order_item[i].product
#         discounted_price = product.discounted_price
#         # order_item[i].total_price = order_item[i].quantity * discounted_price
#         order_item[i].save()
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.product)

class BookRequest(models.Model):
    first_name = models.CharField(max_length=50,default='')
    last_name = models.CharField(max_length=50,default='')
    email = models.CharField(max_length=50,default='')
    phone_no = models.CharField(max_length=50,default='')
    book_name = models.CharField(max_length=50,default='')
    def __str__(self):
        return str(self.first_name)