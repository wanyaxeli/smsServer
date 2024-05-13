from .models import StudentRegistration,FeeSystems,StudentFeeBalance
from django.dispatch import receiver
from rest_framework.response import Response
from django.db.models.signals import post_save,m2m_changed
@receiver(post_save,sender=StudentRegistration)
def InitialstudentBalance(sender,instance,created,**kwargs):
    if created:
        studentClass=instance.Student_class
        try:
             feeSystem=FeeSystems.objects.get(classFee=studentClass)
             studentInitialBalance=StudentFeeBalance.objects.create(student=instance,amount=feeSystem.totalAmount)
             studentInitialBalance.save()
        except FeeSystems.DoesNotExist:
            return  Response('fee system does not exist')