from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from restframe_prac.models import *
from restframe_prac.serializers import *
from rest_framework.authtoken.models import Token
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

# ================================================================================================================================================
# Class Base View
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        std = Student.objects.all()
        serializer = StudentSerializer(std, many=True)
        return Response({"status":200,"message":serializer.data})

    def post(self,request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":200,"message":"Created Successfully!!!"})
        return Response({"status":400,"message":"Invalid Data !!!","error":serializer.errors})

    def put(self,request):
        try:
            id = request.GET.get('id')
            std = Student.objects.get(id = id)
            serializer = StudentSerializer(std,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":200,"message":"Updated Successfully !!!"})
            return Response({'status':400,"message":"Somthing went wrong !!!","error": serializer.errors})
        except Exception as e:
            print(e)
            return Response({"status":400,"message":str(e)})

    def patch(self,request):
        try:
            id = request.GET.get('id')
            std = Student.objects.get(id=id)
            serializer = StudentSerializer(std,data = request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":200,"message":"Updated Successfully !!!"})
            return Response({"status":400,"message":"Somthing went Wrong !!","error":serializer.errors})
        
        except Exception as e:
            print(e)
            return Response({"status":404,"message":"Invalid !!!!","error":str(e)})

    def delete(self,request):
        try:
            id = request.GET.get('id')
            std = Student.objects.get(id=id)
            std.delete()
            return Response({"status":200,"message":"Deleted Successfully !!!"})
        except Exception as e:
            print(e)
            return Response({"status":400,"message":"Invalid !!!","error":str(e)})

class Register(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            user =User.objects.get(username = serializer.data['username'])
            print("User name :: ",user)
            token , created = Token.objects.get_or_create(user=user)
            print(token)
            return Response({"status":200,'payload':serializer.data,'token':str(token),'message':"Successfully Register!!"})
        return Response({"status":400,'message':"Invalid Data !!!","error": serializer.errors})

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class BookAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        book = Book.objects.all()
        serializer = BookSerializer(book,many =True)
        return Response({"status":200,"message":serializer.data})
    
class JWTRegister(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            user =User.objects.get(username = serializer.data['username'])
            print("User name :: ",user)
            # token , created = Token.objects.get_or_create(user=user)
            refresh = RefreshToken.for_user(user)
            print(refresh)
            return Response({"status":200,
                             'payload':serializer.data,
                             'refresh': str(refresh),
                             'access': str(refresh.access_token),
                             'message':"Successfully Register!!"})
        
        return Response({"status":400,'message':"Invalid Data !!!","error": serializer.errors})