
from cgitb import lookup
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Api2.serializer import StudentSerializer
from .models import Student
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView

from rest_framework import viewsets
#url = "http://127.0.0.1:8000/api/list/"


# class Studentgeneric(generics.ListAPIView,generics.CreateAPIView):
   
#     queryset=Student.objects.all()
#     serializer_class = StudentSerializer

# # Create your views here.
# # class StudentViewSet(viewsets.ModelViewSet):
# class StudentGeneric1(generics.UpdateAPIView,generics.DestroyAPIView):
#     queryset=Student.objects.all()
#     serializer_class = StudentSerializer
#     lookup_field='id'

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'stulist': '/',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/stu/pk/delete'
    }
 
    return Response(api_urls)



def list(request):   
    return render(request,'todocreate.html')   

def show_data(request):
    data = Student.objects.all()
    cont = {'data':data}
    return render(request,'show_data.html',cont)

@api_view(['POST'])
def add_student(request):
    ser = StudentSerializer(data = request.data)
    
    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND) 



@api_view(['GET'])
def stu_list(request):
   
    stu_list = Student.objects.all()
    if stu_list:
        serializer_list = StudentSerializer(stu_list, many=True)
        return Response(serializer_list.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['POST','GET','PUT'])
def edit_list(request,pk):     
        
    stu_data = Student.objects.get(id=pk)   
    
    ser_data = StudentSerializer(instance=stu_data,data=request.data)
    
    if ser_data.is_valid():
        
        ser_data.save()
        return Response(ser_data.data)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)    
def data_update(request,pk):
    get_data = Student.objects.get(id=pk)
    cont={'get_data':get_data}
    return render(request,'edit_data.html',cont)
    
def data_delete(request,pk):
    get_data = Student.objects.get(id=pk)
    cont={'get_data':get_data}
    return render(request,'delete.js',cont)


    
@api_view(['GET'])
def detail_info(request,pk): 
    data_stu = Student.objects.get(id=pk)
    ser_data = StudentSerializer(instance=data_stu) 

    return Response(ser_data.data)

@api_view(['DELETE'])
def delete_stu(request,pk):
    stu_id = Student.objects.get(id=pk)
    stu_id.delete()

    return Response(status=status.HTTP_202_ACCEPTED)