from django.contrib import admin
from django.urls import path, include,re_path
from Services import views
app_name='Services'

urlpatterns = [
    re_path(r'^$',views.index,name='index'),

    re_path(r'book-appointment/',views.bookAppointment,\
            name='book_appointment'),
    #services/cardiology
    re_path(r'(?P<category_name>[^%s]*)/',views.serviceInfo,\
          name='service_info')]
