from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def lms_request(request):
    courses = LmsCourse.objects.filter(is_archived = False)
    context = {
        'courses':courses,
        }
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course = LmsCourse.objects.get(name=course_name)
        new_lms_request = LmsRequest.objects.create(
        name =  request.POST.get('name'),
        email =  request.POST.get('email'),
        phone_number =  request.POST.get('phone_no'),
        course_name =  course,
        message =  request.POST.get('message'),
        )
        new_lms_request.save()
        return redirect("/")
    return render(request,"lms_request.html",context)
def lms(request):
    return render(request,"lms.html")