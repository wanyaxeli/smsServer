from django.urls import path
from .views import ClassView,WorkersView,SpecificFeePayment,StudentsView,SubjectsView,StudentFeeBalanceView,FeePaymentView,TeacherView,FeeSystemView
urlpatterns = [
    path('student/',StudentsView.as_view(),name='student'),
    path('teacher/',TeacherView.as_view(),name='teacher'),
    path('feeSystem/',FeeSystemView.as_view(),name='teacher'),
    path('feePayment/',FeePaymentView.as_view(),name='feePayment'),
    path('SpecifcfeePayment/<int:pk>',SpecificFeePayment.as_view(),name='SpecificfeePayment'),
    path('feeBalance/',StudentFeeBalanceView.as_view(),name='feeBalance'),
    path('subjects/',SubjectsView.as_view(),name='subject'),
    path('class/',ClassView.as_view(),name='class'),
    path('worker/',WorkersView.as_view(),name='class'),
]