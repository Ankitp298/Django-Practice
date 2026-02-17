from django.urls import path
from cbv import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.home), 
    path('home/',views.home2), 
    path('fun2/',views.fun2), 
    # path('newfun/',views.newfun),
    path('newfun2/',views.newfun,{"template_name" : "cbv/newfun2.html"}),

    path('cbv/',views.Home.as_view(),name='home'),
    path("cbv2/", views.Home2.as_view(), name="home2"),
    # path("mycbv/", views.Myclasshome.as_view(), name="myclasshome"),
    path("mycbv/", views.Myclasshome.as_view(name = 'Panchal'), name="myclasshome"),
    path("chmycbv/", views.ChildClass.as_view(), name="childclass"),

    path("clfun/", views.clfun.as_view(), name="clfun"),
    path("clfun2/", views.clfun2.as_view(template_name="cbv/newfun2.html"), name="clfun2"),


    # Template Views in CBV

    path("temp-home/", TemplateView.as_view(template_name= "cbv/tempview/home.html"), name="temp-home"),
    # path('temp-home2/',views.TempHome2.as_view(),name='temp-home2'),
    path('temp-home2/<int:id>',views.TempHome2.as_view(),name='temp-home2'),

]
