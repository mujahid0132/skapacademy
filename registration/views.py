from datetime import datetime
from django.shortcuts import render ,redirect
from .models import *
from django.core.files.storage import FileSystemStorage
# Create your views here.
def become_a_tutor(request):
    if request.method == 'POST':
        cnic_image = request.FILES['cnic_image']
        latest_certificate_picture = request.FILES['latest_certificate_picture']
        cv =request.FILES['cv']
        if any(file.size > 2 * 1024 * 1024 for file in [cnic_image, latest_certificate_picture, cv]):
            return redirect('/')
        new_teacher = BecomeATeacher.objects.create(
        email =  request.POST.get('email'),
        name =  request.POST.get('name'),
        gender =  request.POST.get('gender'),
        date_of_birth =  request.POST.get('date_of_birth'),
        phone_number =  request.POST.get('phone_number'),
        whatsapp_number =  request.POST.get('whatsapp_number'),
        years_of_experience =  request.POST.get('years_of_experience'),
        highest_qualification_and_institute =  request.POST.get('highest_qualification_and_institute'),
        educational_background =  request.POST.get('educational_background'),
        other_educational_background = request.POST.get('other_educational_background'),
        can_teach_classes =  request.POST.get('can_teach_classes'),
        can_teach_subjects =  request.POST.get('can_teach_subjects'),
        can_teach_in_areas =  request.POST.get('can_teach_in_areas'),
        can_teach_on_online_platforms =  request.POST.get('can_teach_on_online_platforms'),
        message_or_objective =  request.POST.get('message_or_objective'),
        )
        fs = FileSystemStorage()
        cnic = f'teachers/cnic/{cnic_image.name}{datetime.now().date()}-{datetime.now().time().strftime("%H%M%S")}.png'
        certificate = f'teachers/certificates/{cnic_image.name}{datetime.now().date()}-{datetime.now().time().strftime("%H%M%S")}.png'
        cv_path = f'teachers/cv/{cnic_image.name}{datetime.now().date()}-{datetime.now().time().strftime("%H%M%S")}.png'
        fs.save(cnic, cnic_image , max_length=None)
        fs.save(certificate, latest_certificate_picture , max_length=None)
        fs.save(cv_path, cv , max_length=None)
        new_teacher.cnic_image = cnic
        new_teacher.cv = cv_path
        new_teacher.latest_certificate_picture = certificate
        new_teacher.save()
        return redirect("/success")
    return render(request,"become_a_tutor.html")
def find_a_tutor(request):
    if request.method == 'POST':
        new_student = Student.objects.create(
        name =  request.POST.get('name'),
        email =  request.POST.get('email'),
        subjects_to_study =  request.POST.get('subjects_to_study'),
        phone_number =  request.POST.get('phone_number'),
        whatsapp_number =  request.POST.get('whatsapp_number'),
        student_grade_or_class =  request.POST.get('student_grade_or_class'),
        message =  request.POST.get('message'),
        )
        new_student.save()
        return redirect("/success")
    return render(request,"find_a_tutor.html")