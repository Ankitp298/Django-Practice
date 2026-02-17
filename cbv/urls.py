from django.urls import path
from cbv import views

urlpatterns = [
    path('',views.home), 
    path('home/',views.home2), 
    path('fun2/',views.fun2), 
    # path('newfun/',views.newfun),
    path('newfun2/',views.newfun,{"template_name" : "cbv/newfun2.html"})
]
