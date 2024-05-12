from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StudentRegistration,TeacherRegistration
from .serializers import StudentSerializer,TeacherSerializer
# Create your views here.
class StudentsView(APIView):
    def post(self,request):
        data=request.data
        print('hello4',data)
        regNo=data['regNo']
        first_name=data['first_name']
        middle_name=data['middle_name']
        last_name=data['last_name']
        dob=data['dob']
        Student_class=int(data['class'])
        stream=data['stream']
        parent_first_name=data['parent_first_name']
        parent_last_name=data['parent_last_name']
        parent_phone_number=int(data['phone_number'])
        if  StudentRegistration.objects.filter(first_name=first_name,last_name=last_name,parent_last_name=parent_last_name).exists():
            return Response('student already exists')
        else:
            student=StudentRegistration.objects.create(regNo=regNo,first_name=first_name,middle_name=middle_name,last_name=last_name,
            dob=dob,Student_class=Student_class,stream=stream,parent_first_name=parent_first_name,parent_last_name=parent_last_name,parent_phone_number=parent_phone_number)
            student.save()
            return Response('Student saved succefully')
    def get(self,request):
        students=StudentRegistration.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)

class TeacherView(APIView):
    def post(self,request):
        data=request.data
        employeeNo=data['teacher_no']
        first_name=data['first_name']
        last_name=data['last_name']
        identity=data['id']
        email=data['email']
        gender=data['gender']
        date_of_application=['date_of_appointment']
        subjects=data[' subjects']
        phone_number=data['phone_number']
        print('teacher1',data)
        if TeacherRegistration.objects.filter(identity=identity).exists:
            return Response('teacher already exists')
        else:
            teacher=TeacherRegistration.objects.create(employeeNo=employeeNo,first_name=first_name,last_name=last_name,
            email=email,gender=gender,date_of_application=date_of_application,subjects=subjects,phone_number=phone_number)
            return Response('teacher')