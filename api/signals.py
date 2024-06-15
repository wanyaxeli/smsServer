from .models import User,Profile,StudentRegistration,FeePayment,FeeSystems,StudentFeeBalance
from django.dispatch import receiver
from rest_framework.response import Response
from django.db.models.signals import post_save,m2m_changed
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

@receiver(post_save,sender=User)
def createProfile(sender,instance,created,**kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()

@receiver(post_save,sender=StudentRegistration)
def InitialstudentBalance(sender,instance,created,**kwargs):
    if created:
        studentClass=instance.Student_class
        try:
             feeSystem=FeeSystems.objects.filter(classFee=studentClass).first()
             studentInitialBalance=StudentFeeBalance.objects.create(student=instance,balance=feeSystem.totalAmount,amountPaid=0)
             print('class',studentInitialBalance.student)
             studentInitialBalance.save()
        except FeeSystems.DoesNotExist:
            raise ObjectDoesNotExist('Fee system does not exist for this student class')
@receiver(post_save,sender=StudentFeeBalance)
def intialiFeePayment(sender,instance,created,**kwargs):
    if created:
        student=instance.student
        date=datetime.now()
        print('regno',student)
        studentPaymemt=FeePayment.objects.create(student=student,term=1,teller='none',amount=0,date=date)
        studentPaymemt.save()

@receiver(post_save,sender=FeePayment)
def UpdateFeeBalance(sender,instance,created,**kwargs):
    if created:
        student=instance.student
        amount = instance.amount
        term=instance.term
        print('hello Student',student)
        try:
            feeBalance=StudentFeeBalance.objects.get(student=student)
            feeBalance.balance -=int(amount)
            feeBalance.amountPaid +=int(amount)
            feeBalance.save()
            print('student fee updates successfully')
        except StudentFeeBalance.DoesNotExist:
            raise ObjectDoesNotExist('student does not exist')