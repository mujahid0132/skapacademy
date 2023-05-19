import json
from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse
def shop(request):
    return redirect("/shop/products/")
def productdetail(request,slug):
    product = get_object_or_404(Product, slug=slug)
    images = product.productimage_set.all()
    context = {
        'product': product
        }
    return render(request,"productdetail.html",context)
def products(request):
    productstype = ProductType.objects.filter(is_archived = False)
    params = request.GET
    sortkey = request.GET.get('sort')
    b = Q()
    for key, value in params.items():
        if key == 'sort' or key == "page":
            continue
        q = string_to_q(key,value)
        b = b & q
    if sortkey is None:
        products = Product.objects.filter(b,is_archived = False).order_by('-id')
    else:
        products = Product.objects.filter(b,is_archived = False).order_by(sortkey , 'name')
    paginator = Paginator(products, 20)
    page_number = request.GET.get('page')
    if not page_number:
        page_obj = paginator.get_page(1)
    else:
        page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj,
        'products':products,
        'productstype':productstype,
        }
    return render(request,"products.html",context)
def checkout(request):
    getproducts = request.POST.get('products')
    if getproducts:
        products = json.loads(getproducts)
        product_array = []
        sub_total = 0
        shipping = 200
        for product_id, product_data in products.items():
                name = product_data['name']
                quantity = product_data['quantity']
                product = Product.objects.filter(name=name).first()
                if product:
                    sub_total += (product.discounted_price * quantity)
                    product_array.append({'product': product, 'quantity': quantity})
        total = sub_total + shipping
        context = {
            'product_array': product_array,
            'sub_total': sub_total,
            'shipping': shipping,
            'total': total,
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
        product_get = request.POST.get('products')
        print(first_name)
        if any(var == "" for var in [first_name, last_name, email, phone_no, address, city, country, postal_code, product_get]):
            return JsonResponse({'error': 'One or more required fields are empty.'}, status=400)
        else:
            order = Order.objects.create(first_name = first_name,last_name=last_name,email= email,phone_no = phone_no,address=address,city=city,country=country,postal_code=postal_code)
            products = json.loads(product_get)
            sub_total = 0
            shipping = 200
            for product_id, product_data in products.items():
                    name = product_data['name']
                    quantity = product_data['quantity']
                    product = Product.objects.filter(name=name).first()
                    if product:
                        product.popularity += int(quantity)
                        product.save()
                        OrderItem.objects.create(product=product, order=order, quantity=quantity)
                        sub_total += (product.discounted_price * quantity)
            total = sub_total + shipping
            order.total_price = total
            order.save()
    return redirect("/")
def request_a_book(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        book_name = request.POST.get('book_name')
        if None in [first_name, last_name, email, phone_no, book_name]:
            return redirect("/")
        bookorder = BookRequest.objects.create(first_name = first_name,last_name= last_name,email = email,phone_no=phone_no,book_name=book_name)
        bookorder.save()
        return redirect("/")
    return render(request, 'bookrequest.html')
