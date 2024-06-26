from django.urls import path
from .views import ProfileView,ClassView,ResultsVeiw,UserView,StudentSearch,WorkersView,SpecificFeePayment,StudentsView,SubjectsView,StudentFeeBalanceView,FeePaymentView,TeacherView,FeeSystemView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('student/',StudentsView.as_view(),name='student'),
    path('teacher/',TeacherView.as_view(),name='teacher'),
    path('feeSystem/',FeeSystemView.as_view(),name='teacher'),
    path('feePayment/',FeePaymentView.as_view(),name='feePayment'),
    path('SpecifcfeePayment/<int:pk>',SpecificFeePayment.as_view(),name='SpecificfeePayment'),
    path('feeBalance/',StudentFeeBalanceView.as_view(),name='feeBalance'),
    path('subjects/',SubjectsView.as_view(),name='subject'),
    path('class/',ClassView.as_view(),name='class'),
    path('worker/',WorkersView.as_view(),name='class'),
    path('search/',StudentSearch.as_view(),name='class'),
    path('results/',ResultsVeiw.as_view(),name='results'),
    path('user/',UserView.as_view(),name='user'),
    path('profile/',ProfileView.as_view(),name='profile'),
]