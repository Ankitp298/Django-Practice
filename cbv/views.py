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
    

# ========================================================================================================================
#Redirect View in Django

from django.views.generic import RedirectView,ListView

class SuccessHome(RedirectView):
    pattern_name = 'temp-home'
    query_string = True

class SuccessHome2(RedirectView):
    pattern_name = 'temp-home2'

    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        kwargs['id'] = 22
        return super().get_redirect_url(*args, **kwargs)
    
# ========================================================================================================================
#Genric Display View in Django

from django.views.generic.list import ListView
from cbv.models import Student

class Stdhome(View):
    def get(self,request):
        std = Student.objects.all()
        return render(request,'cbv/genric-display-view/listview.html',{"stds":std})
    
class StdListView(ListView):
    model = Student

class StdListView1(ListView):
    model = Student
    template_name_suffix = '_all'

class StdListView2(ListView):
    model = Student
    template_name = 'cbv/genric-display-view/studentlist.html'

class StdListView3(ListView):
    model = Student
    template_name = 'cbv/genric-display-view/allstudentlist.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.filter(address='HMT')
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['data']= Student.objects.filter(address='AMD')
        return context
    
    def get_template_names(self):
        if self.request.COOKIES.get('user') == 'asd':
            template_name = 'cbv/genric-display-view/asd.html'
        else:
            template_name = self.template_name
        return [template_name]