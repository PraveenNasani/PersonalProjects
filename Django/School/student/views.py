from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm
from .models import StudentData
from django.db.models import Sum,Max
from .serializers import StudentDataSerializer
from rest_framework import generics
# Create your views here.

def home(request):
    return render(request,'home.html')

def student_form(request):
    if request.method=='POST':
        student_data=StudentForm(data=request.POST)
        if student_data.is_valid():
            fname=student_data.cleaned_data['fname']
            student=student_data.save()
            student.save()
            return render(request, 'success.html', context={'fname': fname})
        else:
            student_data = StudentForm()
    else:
        student_data = StudentForm()
    return render(request,'studentform.html',context={'student_form':student_data})

def students_marks(request):
    main_list=[]
    for i in range(1,11):
        x=StudentData.objects.all().filter(grade=i)
        sum_marks=StudentData.objects.filter(grade=i).aggregate(Sum('marks'))
        topper=StudentData.objects.filter(grade=i).aggregate(Max('marks'))
        toppers_list=StudentData.objects.all().filter(grade=i,marks=topper['marks__max'])
        y=[x,sum_marks,i,toppers_list]
        main_list.append(y)
        #print('Grade :',i,'Max marks:',topper)
    #print(main_list)
    print(x)

    return render(request,'students_marks.html',context={'main_list':main_list})


class StudentDataAPIView(generics.ListAPIView):
    queryset = StudentData.objects.all()
    serializer_class = StudentDataSerializer
