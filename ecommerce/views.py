from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.apps import apps
from django.contrib.admin.views.decorators import staff_member_required
from django.template.loader import get_template
def home(request):
    products = Product.objects.order_by('-id')[:5]
    context = {
        'products':products
        }
    return render(request,"home.html",context)
def productdetail(request,slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
        }
    return render(request,"productdetail.html",context)
def products(request):
    productstype = Product.objects.values_list('type',flat=True).distinct()
    print(productstype)
    params = request.GET
    sortkey = request.GET.get('sort')
    b = Q()
    for key, value in params.items():
        if key == 'sort':
            continue
        q = string_to_q(key,value)
        b = b & q
    if sortkey is None:
        products = Product.objects.filter(b).order_by('-id')
    else:
        products = Product.objects.filter(b).order_by(sortkey , 'name')
    context = {
        'products':products,
        'productstype':productstype,
        }
    return render(request,"products.html",context)
def checkout(request):
    products = request.POST.get("products")
    if products is None:
        return redirect("/")
    q = string_to_q("name",products)
    prod = Product.objects.filter(q)
    if prod.exists():
        context = {
            'products':prod
            }
        return render(request,"checkout.html",context)
    return redirect("/")
def string_to_q(key,value):
    parts = value.split("_")
    q_objects = Q()
    for part in parts:
        q_objects |= Q(**{key: part})
    return q_objects
def complete_order(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('country')
        postal_code = request.POST.get('postal_code')
        products = request.POST.get('product')
        quantities = request.POST.get('quantity')
        order = Order.objects.create(first_name = first_name,last_name=last_name,email= email,phone_no = phone_no,address=address,city=city,country=country,postal_code=postal_code)
        quantities_list = quantities.split(",")
        products_list = products.split(",")
        total = 0
        for i in range(len(products_list)):
            product = Product.objects.get(name=products_list[i])
            print(product.popularity)
            product.popularity += int(quantities_list[i])
            print(product.popularity)
            product.save()
            total += (product.discounted_price)*int(quantities_list[i])
            OrderItem.objects.create(product=product, order=order, quantity=quantities_list[i])
        order.total_price = total
        order.save()
        return render(request, 'base.html')
    return redirect("/")
def test(request):
    product_types = ProductType.objects.all()
    context = {
        'product_types':product_types,
        }
    return render(request,"test.html",context)
@staff_member_required
def showdates(request,db_table):
    table = db_table_seperator(db_table)
    dates = table[1].objects.dates(table[2],'day')
    print(dates)
    context = {
        'dates':dates,
        'model':table[2]
        }
    return render(request,"orders-download.html",context)
@staff_member_required
def detail(request,db_table,date):
    table = db_table_seperator(db_table)
    objects = table[1].objects.filter(**{f'{table[2]}__date': date})
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
def request_a_book(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        book_name = request.POST.get('book_name')
        bookorder = BookRequest.objects.create(first_name = first_name,last_name= last_name,email = email,phone_no=phone_no,book_name=book_name)
        bookorder.save()
        return render(request, 'bookrequest.html')
    return render(request, 'bookrequest.html')