from django.db import models
from django.core.exceptions import ValidationError
class BecomeATeacher(models.Model):
    email = models.EmailField( max_length=254,default="")
    name = models.CharField(max_length=50,default="")
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(
        max_length=6,
        choices=gender_choices,
        default='male')
    date_of_birth = models.DateField()
    date_of_form_submission = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=50,default="")
    whatsapp_number = models.CharField(max_length=50,default="")
    years_of_experience_choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('1', '1'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10+', '10+'),
    ]
    years_of_experience = models.CharField(
        max_length=3,
        choices=years_of_experience_choices,
        default='1'
        )
    highest_qualification_and_institute = models.CharField(max_length=50,default="")
    educational_background = models.CharField(max_length=50,default="")
    educational_background_choices = [
        ('olevel_igcse_alevel', 'O level, IGCSE/ A level'),
        ('matric_fsc', 'Matric / FSc'),
        ('other', 'Other'),
    ]
    educational_background = models.CharField(
        max_length=19,
        choices=educational_background_choices,
        default='matric_fsc'
        )
    other_educational_background = models.CharField(max_length=255, blank=True)
    can_teach_classes = models.CharField(max_length=50,default="")
    can_teach_subjects = models.CharField(max_length=50,default="")
    can_teach_in_areas = models.CharField(max_length=50,default="")
    can_teach_on_online_platforms = models.CharField(max_length=50,default="")
    message_or_objective = models.TextField()
    cnic_image = models.ImageField(upload_to="teachers/cnic/",default="/products/default/default.png")
    latest_certificate_picture = models.ImageField(upload_to="teachers/certificates/",default="/products/default/default.png")
    cv = models.FileField(upload_to="techers/cv/",default="/products/default/default.png")
    def clean(self):
        if self.educational_background == "other" and self.other_educational_background == "":
            raise ValidationError('You must specify other educational background')
    def __str__(self):
        return str(self.name)
class Student(models.Model):
    name = models.CharField(max_length=255,default="")
    email = models.EmailField( max_length=254,default="")
    subjects_to_study = models.CharField(max_length=255,default="")
    phone_number = models.CharField(max_length=255,default="")
    whatsapp_number = models.CharField(max_length=255,default="",null= True)
    student_grade_or_class = models.CharField(max_length=255,default="")
    message = models.TextField(default="")
    date_of_form_submission = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)


