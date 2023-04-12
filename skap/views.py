from .models import *
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.apps import apps

def home(request):
    return render(request,"home.html")

def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")
def success(request):
    return render(request,"about.html")
def blog(request):
    return render(request,"blog.html")

@staff_member_required
def showdates(request,db_table):
    table = db_table_seperator(db_table)
    dates = table[1].objects.dates(table[2],'day').filter(is_archived = False)
    print(dates)
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