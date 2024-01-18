from django.shortcuts import render
from django.urls import path
from StudentApp import views

# Create your views here.
urlpatterns = [
    path('', views.login_fun, name='log'),
    path('reg', views.reg_fun, name='reg'),
    path('home', views.home_fun, name='home'),
    path("add_course", views.addcourse_fun, name="add_course"),
    path("display_course", views.displaycourse_fun, name="display_course"),
    path("update_course/<int:courseid>", views.updatecourse_fun, name="update_course"),
    path("delete_course/<int:courseid>", views.deletecourse_fun, name="delete_course"),
    path("add_student", views.addstudent_fun, name="add_student"),
    path("displaystudent", views.displaystudent_fun, name="displaystudent"),
    path("updatestudent/<int:stud_id>", views.updatestudent_fun, name="updatestudent"),
    path("deletestudent/<int:stud_id>", views.deletestudent_fun, name="deletestudent"),
    path("logout", views.logout_fun, name="logo")

    ]