from django.shortcuts import render
from .models import *
# Create your views here.
def lsm_request(request):
    courses = LmsCourse.objects.all()
    context = {
        'courses':courses,
        }
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course = LmsCourse.objects.get(name=course_name)
        print(request.POST.get('course_name'))
        new_lms_request = LmsRequest.objects.create(
        name =  request.POST.get('name'),
        email =  request.POST.get('email'),
        phone_number =  request.POST.get('phone_number'),
        course_name =  course,
        message =  request.POST.get('message'),
        )
        new_lms_request.save()
        return render(request, 'base.html')
    return render(request,"lms_request.html",context)