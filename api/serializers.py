from .models import Classes,Profile,User,Results,WorkersRegistration,StudentRegistration,Subjects,StudentFeeBalance,FeePayment,TeacherRegistration,FeeSystems
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, Permission
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['first_name', 'email', 'last_name', 'phone_number', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
        }
    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError("The passwords do not match.")
        
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Remove confirm_password since it is not a model field
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    #     return data
    # def validate_password(self, value):
    #     return make_password(value)
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['user_id'] = user.pk

        return token
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentRegistration
        fields='__all__'
class UserDetails(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','email','phone_number']
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
class ProfileSerializer(serializers.ModelSerializer):
    user=UserDetails()
    class Meta:
        model=Profile
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

class ResultsSerializer(serializers.ModelSerializer):
    student=StudentDetailsSerializer()
    class Meta:
        model=Results
        fields='__all__'