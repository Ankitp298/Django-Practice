from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def home(request):
    return HttpResponse("this is Homepage")

class Home(View):
    def get(self,request):
        return HttpResponse('This is Class Base View !!! ')

def home2(request):
    return HttpResponse("<h1> this is Homepage </h1>")

class Home2(View):
    def get(self,request):
        return HttpResponse("<h1> this is Homepage </h1>")

class Myclasshome(View):
    name = "Ankit"
    def get(self,request):
        return HttpResponse(f"Name : {self.name}")
    
class ChildClass(Myclasshome):
    def get(self, request):
        return HttpResponse(f"From Child Class Name : {self.name}")

def fun2(request):
    context = {'msg': "this is context from Function base view!!"}
    return render(request,'cbv/fun2.html',context)

class clfun(View):
    def get(self,request):
        context = {'msg': "this is context from Class base view!!"}
        return render(request,'cbv/fun2.html',context)
        

def newfun(request,template_name):
    template_name = template_name
    context = {'newmsg': "this is New Funcation context from Function base view!!"}
    return render(request,template_name,context)

class clfun2(View):
    template_name = ''
    context = {'newmsg': "this is New Class context from Class base view!!"}
    def get(self,request):
        return render(request,self.template_name,context=self.context)
    
# def newfun(request):
#     template_name = "cbv/newfun.html"
#     context = {'newmsg': "this is context from Function base view!!"}
#     return render(request,template_name,context)


# ========================================================================================================================
#Template View in Django

from django.views.generic import TemplateView

class TempHome2(TemplateView):
    template_name = 'cbv/tempview/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Ankit"
        context['roll'] = 123
        print(context)
        print(kwargs)
        return context