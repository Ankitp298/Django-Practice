from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("this is Homepage")

def home2(request):
    return HttpResponse("<h1> this is Homepage </h1>")

def fun2(request):
    context = {'msg': "this is context from Function base view!!"}
    return render(request,'cbv/fun2.html',context)

def newfun(request,template_name):
    template_name = template_name
    context = {'newmsg': "this is New Funcation context from Function base view!!"}
    return render(request,template_name,context)

# def newfun(request):
#     template_name = "cbv/newfun.html"
#     context = {'newmsg': "this is context from Function base view!!"}
#     return render(request,template_name,context)
