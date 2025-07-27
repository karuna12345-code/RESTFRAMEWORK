from django.urls import path
from .views.main_view import add_student, get_student, update, get_stu, delete_stu, add_employee, get_employeee, update, delete_employee

urlpatterns = [
    path('add/',add_student),
    path('get/',get_student),
    path('update/<int:id>', update),
    path('get_stu/<int:id>',get_stu),
    path('delete_stu/<int:id>',delete_stu),
    path('add_employee/',add_employee),
    path('get_employee/', get_employeee),
    path('update_employee/<int:id>',update),
    path('delete_employee/<int:id>', delete_employee)
]
