from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone_number=models.IntegerField(default=0)
    confirm_password=models.CharField(max_length=255,null=True)
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
class StudentRegistration(models.Model):
    regNo=models.CharField(max_length=255,default='')
    first_name=models.CharField(max_length=255,default='')
    middle_name=models.CharField(max_length=255,default='',null=True,blank=True)
    last_name=models.CharField(max_length=255,default='',null=True,blank=True)
    dob=models.DateField(default=datetime.now)
    Student_class=models.IntegerField(default=0)
    stream=models.CharField(max_length=255,null=True)
    parent_first_name=models.CharField(max_length=255,null=True)
    parent_last_name=models.CharField(max_length=255,null=True)
    parent_phone_number=models.IntegerField(default=0,null=True)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
class Subjects(models.Model):
    name=models.CharField(max_length=255,null=True)
    def __str__(self) -> str:
        return self.name
class Classes(models.Model):
    name=models.CharField(max_length=255,null=True)
    stream=models.CharField(max_length=255,null=True)
    def __str__(self) -> str:
        return self.name
class FeeSystems(models.Model):
    classFee=models.IntegerField(default=0)
    term_one=models.IntegerField(default=0)
    term_two=models.IntegerField(default=0)
    term_three=models.IntegerField(default=0)
    totalAmount=models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.classFee
class FeePayment(models.Model):
    student=models.ForeignKey(StudentRegistration,on_delete=models.CASCADE)
    term=models.IntegerField(default=1)
    amount=models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.student

class TeacherRegistration(models.Model):
    employeeNo=models.CharField(max_length=255,default='')
    first_name=models.CharField(max_length=255,default='')
    last_name=models.CharField(max_length=255,default='')
    identity=models.IntegerField(default=0)
    email=models.EmailField(max_length=255,null=True)
    gender=models.CharField(max_length=255,null=True)
    date_of_application=models.DateField(default=datetime.now)
    phone_number=models.IntegerField(default=0)
    subjects=models.CharField(max_length=500,default='')
    # Subject=models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
class WorkersRegistration(models.Model):
    first_name=models.CharField(max_length=255,default='')
    last_name=models.CharField(max_length=255,default='')
    identity=models.IntegerField(default=0)
    phone_number=models.IntegerField(default=0)
    email=models.EmailField(max_length=255,null=True)
    work=models.CharField(max_length=255,null=True)
    gender=models.CharField(max_length=255,null=True)
    date_of_application=models.DateField(default=datetime.now)
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
class Results(models.Model):
    student=models.ForeignKey(StudentRegistration,on_delete=models.CASCADE)
    subject=models.CharField(max_length=255)
    marks=models.IntegerField(default=0)