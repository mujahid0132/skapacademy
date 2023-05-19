from ecommerce.models import Product
from .models import *
from django.shortcuts import render,redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.apps import apps
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

def home(request):
    products = Product.objects.all().order_by('id')[:8]
    testimonial = Testimonial.objects.all()
    context = {
        "products":products,
        "testimonial":testimonial
    }
    return render(request,"home.html",context)
def blog_detail(request,slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = {
        'blog': blog
        }
    return render(request,"blog_detail.html",context)
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        message = request.POST.get('message')
        contact= Contact.objects.create(name =name,email=email,phone_no= phone_no,message=message)
        contact.save()
        return redirect("/")
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")
def success(request):
    return render(request,"about.html")
def blog(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    if not page_number:
        page_obj = paginator.get_page(1)
    else:
        page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj,
        }
    return render(request,"blog.html",context)

@staff_member_required
def showdates(request,db_table):
    table = db_table_seperator(db_table)
    dates = table[1].objects.dates(table[2],'day').filter(is_archived = False)
    context = {
        'dates':dates,
        'model':table[2]
        }
    return render(request,"download.html",context)
@staff_member_required
def detail(request,db_table,date):
    table = db_table_seperator(db_table)
    objects = table[1].objects.filter(**{f'{table[2]}__date': date,'is_archived': False})
    context = {
        'objects':objects,
        }
    template = f"{table[1]._meta.model_name}detailpdf.html"
    return render(request,template,context)
def db_table_seperator(db_table):
    words = db_table.split("_")
    model = words[1]
    appname = words[0]
    model_name = apps.get_model(app_label=appname, model_name=model)
    for field in model_name._meta.fields:
        if isinstance(field, models.DateTimeField):
            date_time_field_name = field.name
            break
    return [appname,model_name,date_time_field_name]