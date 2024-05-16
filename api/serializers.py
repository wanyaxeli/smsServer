from .models import Classes,WorkersRegistration,StudentRegistration,Subjects,StudentFeeBalance,FeePayment,TeacherRegistration,FeeSystems
from rest_framework import serializers
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentRegistration
        fields='__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeacherRegistration
        fields='__all__'
class FeeSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model=FeeSystems
        fields='__all__'
class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentRegistration
        fields=['id','regNo','first_name','last_name','Student_class','stream']
class FeePaymentSerializer(serializers.ModelSerializer):
    student=StudentDetailsSerializer()
    class Meta:
        model=FeePayment
        fields='__all__'

class StudentFeeBalanceSerializer(serializers.ModelSerializer):
    student=StudentDetailsSerializer()
    class Meta:
        model=StudentFeeBalance
        fields='__all__'
class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subjects
        fields='__all__'
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model=Classes
        fields='__all__'
class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model=WorkersRegistration
        fields='__all__'