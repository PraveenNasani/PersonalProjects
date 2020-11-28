from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home),
    path('student_form/',views.student_form,name='student_form'),
    path('students_marks/',views.students_marks,name='students_marks'),
    path('api/',views.StudentDataAPIView.as_view()),
]