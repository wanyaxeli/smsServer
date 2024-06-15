from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Classes,Results,Profile,User,WorkersRegistration,StudentFeeBalance,Subjects,StudentRegistration,TeacherRegistration,FeeSystems,FeePayment
from .serializers import ProfileSerializer,MyTokenObtainPairSerializer,WorkerSerializer,UserSerializer,ResultsSerializer,ClassSerializer,SubjectsSerializer,StudentFeeBalanceSerializer,FeePaymentSerializer,StudentSerializer,TeacherSerializer,FeeSystemSerializer
from django.db.models import Count
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer
class UserView(APIView):
    def post(self, request):
        data = request.data['data']
        first_name = data['first_name']
        email = data['email']
        last_name = data['last_name']
        phone_number = data['phone_number']
        password = data['password']
        confirm_password = data['confirm_password']

        if password != confirm_password:
            print('asdas',password)
            return Response({'error': 'Passwords do not match'})
    
        if User.objects.filter(first_name=first_name, last_name=last_name).exists():
            return Response({'error': 'Account already exists'})
        elif User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists'})
        else:
           
            serializer = UserSerializer(data={
                'first_name': first_name,
                'email': email,
                'last_name': last_name,
                'phone_number': phone_number,
                'password': password,
                'confirm_password': confirm_password
            })

            if serializer.is_valid():
                serializer.save()
                return Response({'success': 'Account created successfully'})
            else:
                return Response({'error':serializer.errors})
    def get(self,request):
        user=User.objects.all()
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)
    def delete(self,request):
        user=User.objects.all()
        user.delete()

class ProfileView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        user=request.user
        try:
            profile=Profile.objects.get(user=user)
            serilizer=ProfileSerializer(profile)
            return Response(serilizer.data)
        except Profile.DoesNotExist:
            return Response('profile not exist')
 
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
        employeeNo=data['teacher_no']
        first_name=data['first_name']
        last_name=data['last_name']
        identity=data['id']
        email=data['email']
        gender=data['gender']
        date_of_application=data['date_of_appointment']
        subjects=data['subjects']
        phone_number=data['phone_number']
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
        employee_earning=data['employee_earning']
        date_of_application=data['date_of_appointment']
        phone_number=data['phone_number']
        print('teacher1',date_of_application)
        if WorkersRegistration.objects.filter(identity=identity).exists():
            return Response('worker already exists')
        else:
            worker=WorkersRegistration.objects.create(first_name=first_name,last_name=last_name,email=email,identity=identity,gender=gender,date_of_application=date_of_application,employee_earning=employee_earning,phone_number=phone_number)
            worker.save()
            return Response('worker added successfully')
    def get(self,request):
        workers=WorkersRegistration.objects.all()
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
class StudentSearch(APIView):
    def post(self,request):
        data=request.data['regNo']
        print(data)
        try:
            student=StudentRegistration.objects.get(regNo=data)
            serializer=StudentSerializer(student)
            return Response(serializer.data)
        except StudentRegistration.DoesNotExist:
            return Response('student does not exist')


class ResultsVeiw(APIView):
    def post(self,request):
        data=request.data['values']
        regNo=data['regNo']
        subject=data['subject']
        marks=data['marks']
        try:
            student = StudentRegistration.objects.get(regNo=regNo)
        except StudentRegistration.DoesNotExist:
            return Response({'error': 'Student not found'})

        try:
            subject = Subjects.objects.get(name=subject)
        except Subjects.DoesNotExist:
            return Response({'error': 'Subject not found'})

        results, created = Results.objects.update_or_create(
            student=student,
            subject=subject,
            marks= marks
        )

        if created:
            message = 'Results recorded successfully'
        else:
            message = 'Results updated successfully'

        return Response({'message': message})
    def get(self,request):
        students = StudentRegistration.objects.filter(results__isnull=False).distinct()
        all_students_data = []

        for student in students:
            results = Results.objects.filter(student=student).select_related('subject')
            if results.exists():
                results_data = [
                    {
                        'subject': result.subject.name,
                        'marks': result.marks
                    }
                    for result in results
                ]

                student_data = {
                    'id': student.id,
                    'regNo': student.regNo,
                    'first_name': student.first_name,
                    'last_name': student.last_name,
                    'Student_class': student.Student_class,
                    'results': results_data
                }
                all_students_data.append(student_data)

        return Response(all_students_data)