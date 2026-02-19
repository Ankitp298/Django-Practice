from django.urls import path
from restframe_prac import views

urlpatterns = [
    path('',views.rest_home,name='rest_home'),
    path('get-student/<int:id>/',views.get_student_by_id,name='get_student_by_id'),
    path('post-student/',views.post_student,name='post_student'),
    path('update-student/<int:id>/',views.update_student,name='update-student'),
    path('partial-student/<int:id>/',views.partial_update_student,name='partial-update-student'),
    path('delete-student/<int:id>/',views.delete_student,name='delete-student'),

    path("book/",views.get_all_book,name="get_all_book"),

# ================================================================================================================================================
# Class Base View

    path('student/',views.StudentAPI.as_view(),name='student'),
]
