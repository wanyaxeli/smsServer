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
    dob=models.DateField(default=datetime.now,blank=True, null=True)
    Student_class=models.IntegerField(default=0)
    stream=models.CharField(max_length=255,null=True)
    parent_first_name=models.CharField(max_length=255,null=True)
    parent_last_name=models.CharField(max_length=255,null=True)
    parent_phone_number=models.IntegerField(default=0,null=True)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
class Subjects(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name

class Classes(models.Model):
    name=models.CharField(max_length=255,null=True)
    stream=models.CharField(max_length=255,null=True)
    def __str__(self) -> str:
        return f'class {self.name} {self.stream}'
class FeeSystems(models.Model):
    classFee=models.IntegerField(default=0)
    term_one=models.IntegerField(default=0)
    term_two=models.IntegerField(default=0)
    term_three=models.IntegerField(default=0)
    totalAmount=models.IntegerField(default=0)
    def __str__(self) -> str:
        return f'class {self.classFee}'
class FeePayment(models.Model):
    student=models.ForeignKey(StudentRegistration,on_delete=models.CASCADE)
    term=models.IntegerField(default=1)
    amount=models.IntegerField(default=0)
    teller=models.CharField(max_length=255,default='')
    date=models.DateField(default=datetime.now)
    def __str__(self) -> str:
        return f'{self.student.first_name} {self.student.last_name}'

class TeacherRegistration(models.Model):
    employeeNo=models.CharField(max_length=255,default='')
    first_name=models.CharField(max_length=255,default='')
    last_name=models.CharField(max_length=255,default='')
    identity=models.IntegerField(default=0)
    email=models.EmailField(max_length=255,default='')
    gender=models.CharField(max_length=255,default='')
    date_of_application=models.DateField(default=datetime.now)
    phone_number=models.IntegerField(default=0)
    subjects=models.CharField(max_length=255,default='')
   

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
    employee_earning=models.IntegerField(default=0)
    date_of_application=models.DateField(default=datetime.now)
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
class Results(models.Model):
    student=models.ForeignKey(StudentRegistration,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subjects,on_delete=models.CASCADE,default='')
    marks=models.IntegerField(default=0)
    class Meta:
        unique_together = ('student', 'subject')
    def __str__(self):
        return f"{self.student.first_name}  {self.subject.name} - {self.marks}"
class StudentFeeBalance(models.Model):
    student=models.ForeignKey(StudentRegistration,on_delete=models.CASCADE)
    balance=models.IntegerField(default='')
    amountPaid=models.IntegerField(default='')