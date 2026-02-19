from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from restframe_prac.models import *
from restframe_prac.serializers import *
# Create your views here.

@api_view()
def rest_home(request):
    std = Student.objects.all()
    serializer = StudentSerializer(std, many = True)
    print(serializer.data)
    return Response({"status":200, "message": serializer.data})

@api_view(['GET'])
def get_student_by_id(request,id):
    try:
        std = Student.objects.get(id=id)
        serializer = StudentSerializer(std)
        print(serializer.data)
        return Response({"status":200,"message":serializer.data})
    except Exception as e:
        return Response({"status":404,"message":"Not Found!!"})
    
@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": 200, 'message':'data saved !!!'})

    return Response({"status":300,'message':'somthing went wrong!!',"error": serializer.errors})
    
@api_view(['PUT'])
def update_student(request,id):
    try:
        std = Student.objects.get(id = id)
        serializer = StudentSerializer(std,data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":200,"message":"Data Updated !!"})
    except Exception as e:
        print(e)
        raise ValueError({"error": "Id not found!!!"})
    return Response({"status":300,"message":'Somthing went wrong !!!',"error":serializer.errors})

@api_view(['PATCH'])
def partial_update_student(request,id):
    try:
        std = Student.objects.get(id = id)
        serializer = StudentSerializer(std,data =request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":200,"message":"Data Updated !!"})
    except Exception as e:
        print(e)
        raise ValueError({"error": "Id not found!!!"})
    return Response({"status":300,"message":'Somthing went wrong !!!',"error":serializer.errors})

@api_view(['DELETE'])
def delete_student(request,id):
    try:
        std = Student.objects.get(id=id)
        std.delete()
        return Response({"status":200,"message":"Deleted Successfully!!"})
    except Exception as e:
        print(e)
        return Response({"error":e})
    

@api_view()
def get_all_book(request):
    book = Book.objects.all()
    serializer = BookSerializer(book,many= True)
    return Response({"status":200,"message":serializer.data})