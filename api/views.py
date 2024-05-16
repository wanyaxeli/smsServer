from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Classes,WorkersRegistration,StudentFeeBalance,Subjects,StudentRegistration,TeacherRegistration,FeeSystems,FeePayment
from .serializers import WorkerSerializer,ClassSerializer,SubjectsSerializer,StudentFeeBalanceSerializer,FeePaymentSerializer,StudentSerializer,TeacherSerializer,FeeSystemSerializer
from django.db.models import Count
# Create your views here.
class StudentsView(APIView):
    def post(self,request):
        data=request.data
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
        print('data',data)
        employeeNo=data['teacher_no']
        first_name=data['first_name']
        last_name=data['last_name']
        identity=data['id']
        email=data['email']
        gender=data['gender']
        date_of_application=data['date_of_appointment']
        subjects=data['subjects']
        phone_number=data['phone_number']
        print('teacher1',date_of_application)
        if TeacherRegistration.objects.filter(employeeNo=employeeNo,identity=identity).exists():
            return Response('teacher already exists')
        else:
            teacher=TeacherRegistration.objects.create(employeeNo=employeeNo,first_name=first_name,last_name=last_name,email=email,identity=identity,gender=gender,date_of_application=date_of_application,subjects=subjects,phone_number=phone_number)
            teacher.save()
            return Response('teacher added successfully')
    def get(self,request):
        teachers=TeacherRegistration.objects.all()
        serializer=TeacherSerializer(teachers,many=True)
        return Response(serializer.data)
class FeeSystemView(APIView):
    def post(self,request):
        data=request.data
        classFee=int(data['classFee'])
        term_one=int(data['term_one'])
        term_two=int(data['term_two'])
        term_three=int(data['term_three'])
        totalAmount=int(data['totalAmount'])
        print('fee',data)
        if FeeSystems.objects.filter(classFee=classFee).exists():
            return Response('class fee exists')
        else:
            fee=FeeSystems.objects.create(classFee=classFee,term_one=term_one,term_two=term_two,term_three=term_three,totalAmount=totalAmount)
            fee.save()
            return Response('fee system created successfully')
    def get(self,request):
        feeSystem=FeeSystems.objects.all()
        serializer=FeeSystemSerializer(feeSystem,many=True)
        return Response(serializer.data)

class FeePaymentView(APIView):
    def post(self,request):
        data=request.data
        regNo=data['regNo']
        term=data['term']
        amount=data['amount']
        teller=data['teller']
        date=data['date']
        try:
            student=StudentRegistration.objects.get( regNo=regNo)
            feePayment=FeePayment.objects.create(student=student,term=term,teller=teller,date=date,amount=amount)
            feePayment.save()
            return Response(f'fee payment of {student.first_name} {student.first_name} recorded successfully')
        except StudentRegistration.DoesNotExist:
            return Response('student does not exist')
    def get(self,request):
        feepaymemt=FeePayment.objects.all()
        serializer=FeePaymentSerializer(feepaymemt,many=True)
        return Response(serializer.data)

class StudentFeeBalanceView(APIView):
    def get(self,request):
        feeBalance=StudentFeeBalance.objects.all()
        serializer=StudentFeeBalanceSerializer(feeBalance,many=True)
        return Response(serializer.data)

class SubjectsView(APIView):
    def post(self,request):
        data=request.data['name']
        print(data)
        if Subjects.objects.filter(name=data).exists():
            return Response('subject already exists')
        else :
            subject=Subjects.objects.create(name=data)
            subject.save()
            return Response('subject saved')
    def get(self,request):
        subjects=Subjects.objects.all()
        serializer=SubjectsSerializer(subjects,many=True)
        return Response(serializer.data)

class ClassView(APIView):
    def post(self,request):
        data=request.data
        print('class',data)
        name=data['name']
        stream=data['stream']
        if Classes.objects.filter(name=name,stream=stream).exists():
            return Response('class exists')
        else:
            classes=Classes.objects.create(name=name,stream=stream)
            classes.save()
            return Response('class created successfully')
    def get(self,request):
        classes=Classes.objects.all()
        serializer=ClassSerializer(classes,many=True)
        return Response(serializer.data)

class WorkersView(APIView):
    def post(self,request):
        data=request.data
        print('data',data)
        first_name=data['first_name']
        last_name=data['last_name']
        identity=data['id']
        email=data['email']
        gender=data['gender']
        date_of_application=data['date_of_appointment']
        phone_number=data['phone_number']
        print('teacher1',date_of_application)
        if WorkersRegistration.objects.filter(identity=identity).exists():
            return Response('worker already exists')
        else:
            worker=WorkersRegistration.objects.create(first_name=first_name,last_name=last_name,email=email,identity=identity,gender=gender,date_of_application=date_of_application,phone_number=phone_number)
            worker.save()
            return Response('worker added successfully')
    def get(self,request):
        workers=TeacherRegistration.objects.all()
        serializer=WorkerSerializer(workers,many=True)
        return Response(serializer.data)
class SpecificFeePayment(APIView):
    def get(self,request,*args,**kwargs):
        pk=self.kwargs['pk']
        try:
            student=StudentRegistration.objects.get(pk=pk)
            feePayment=FeePayment.objects.get(student=student)
            serializer=FeePaymentSerializer(feePayment)
            return Response(serializer.data)
        except StudentRegistration.DoesNotExist:
            return Response('student does not exist')
