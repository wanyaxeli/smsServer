from django.urls import path
from .views import StudentsView,TeacherView,FeeSystemView
urlpatterns = [
    path('student/',StudentsView.as_view(),name='student'),
    path('teacher/',TeacherView.as_view(),name='teacher'),
    path('feeSystem/',FeeSystemView.as_view(),name='teacher')
]
