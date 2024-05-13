from .models import StudentRegistration,FeePayment,FeeSystems,StudentFeeBalance
from django.dispatch import receiver
from rest_framework.response import Response
from django.db.models.signals import post_save,m2m_changed
from django.core.exceptions import ObjectDoesNotExist
@receiver(post_save,sender=StudentRegistration)
def InitialstudentBalance(sender,instance,created,**kwargs):
    if created:
        studentClass=instance.Student_class
        try:
             feeSystem=FeeSystems.objects.get(classFee=studentClass)
             studentInitialBalance=StudentFeeBalance.objects.create(student=instance,amount=feeSystem.totalAmount)
             print('class',studentInitialBalance.student)
             studentInitialBalance.save()
        except FeeSystems.DoesNotExist:
            raise ObjectDoesNotExist('Fee system does not exist for this student class')

@receiver(post_save,sender=FeePayment)
def UpdateFeeBalance(sender,instance,created,**kwargs):
    if created:
        student=instance.student
        amount = instance.amount
        print('hello Student',student)
        try:
            feeBalance=StudentFeeBalance.objects.get(student=student)
            feeBalance.amount -=int(amount)
            feeBalance.save()
            print('student fee updates successfully')
        except StudentFeeBalance.DoesNotExist:
            raise ObjectDoesNotExist('student does not exist')