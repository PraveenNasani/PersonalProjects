from django.db import models

# Create your models here.
class Service(models.Model):
    category=models.CharField(max_length=250)
    Fee=models.DecimalField(max_digits=5,decimal_places=2)
    category_pic=models.CharField(max_length=10000)

    def __str__(self):
        return self.category

class Doctor(models.Model):
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    qualification=models.CharField(max_length=250)
    experience=models.CharField(max_length=100)
    doctor_pic=models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=250)
    patient_age=models.IntegerField()
    appointment_time=models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.patient_name + ' at ' \
               + str(self.appointment_time) + \
               'with Dr.' +self.doctor.name