from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
#from services.models import Services
# Create your views here.
from Services.models import Service,Appointment,Doctor
from . serializers import appointmentSerializer


def index(request):
   # html='<h1>Welcome to CURE Hospitals</h1>'
   all_services=Service.objects.all()
   all_doctors=Doctor.objects.all()
   context={'all_services':all_services,'all_doctors':all_doctors
            }
   template=loader.get_template('services/index.html')
   return HttpResponse(template.render(context,request))

def serviceInfo(request,category_name):

   service=Service.objects.get(category=category_name)
   context= {'service':service}
   template=loader.get_template('services/service_info.html')
   return HttpResponse(template.render(context, request))

def bookAppointment(request):
   new_app=Appointment()
   new_app.doctor=Doctor.objects.get(pk=request.POST.get('doctor_name'))
   new_app.appointment_time=request.POST.get('your_time')
   new_app.patient_name=request.POST.get('your_name')
   new_app.patient_age=request.POST.get('your_age')
   new_app.save()
   return HttpResponseRedirect(reverse('Services:index'))

class appointmentList(APIView):
   def get(self,request):
      appointments=Appointment.objects.all()
      serializer=appointmentSerializer(appointments,many=True)
      return Response(serializer.data)
