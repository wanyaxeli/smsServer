from .models import StudentRegistration,TeacherRegistration
from rest_framework import serializers
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentRegistration
        fields='__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeacherRegistration
        fields='__all__'