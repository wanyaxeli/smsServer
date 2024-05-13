from django.contrib import admin
from .models import User,StudentFeeBalance,StudentRegistration,Subjects,Classes,FeeSystems,FeePayment,TeacherRegistration,WorkersRegistration,Results
admin.site.register(User)
admin.site.register(StudentRegistration)
admin.site.register(Subjects)
admin.site.register(Classes)
admin.site.register(FeePayment)
admin.site.register(FeeSystems)
admin.site.register(TeacherRegistration)
admin.site.register(WorkersRegistration)
admin.site.register(Results)
admin.site.register(StudentFeeBalance)
# Register your models here.
