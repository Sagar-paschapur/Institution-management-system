from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from StudentApp.models import Course, City, Student


@never_cache
def login_fun(request):
    if request.method == "POST":
        u_name = request.POST["txtUser"]
        u_pass = request.POST["txtPass"]
        u1 = authenticate(username=u_name, password=u_pass)
        if u1 is not None:
            if u1.is_superuser:
                request.session['uname'] = u_name
                login(request, u1)
                return redirect("home")

        else:
            return render(request, "login.html", {"msg": "username or password is incorrect"})
    else:
        return render(request, "login.html")


@never_cache
def reg_fun(request):
    if request.method == "POST":
        u_name = request.POST["txtUser"]
        u_pass = request.POST["txtPass"]
        u_mail = request.POST["txtEmail"]
        if User.objects.filter(username=u_name).exists():
            return render(request, 'register.html', {"msg": "user already exists!"})
        else:
            u1 = User.objects.create_superuser(username=u_name, password=u_pass, email=u_mail)
            u1.save()
            return redirect("log")
    else:
        return render(request, "register.html")


@login_required
@never_cache
def home_fun(request):
    return render(request, "home.html", {"data": request.session['uname']})


@login_required
@never_cache
def addcourse_fun(request):
    if request.method == "POST":
        c1 = Course()
        c1.course_name = request.POST['txtCourseName']
        c1.course_duration = request.POST['txtCourseDuration']
        c1.course_fees = int(request.POST['txtCourseFees'])
        c1.save()
        return render(request, "addcourse.html", {'msg': "succesfully added"})
    else:
        return render(request, "addcourse.html")


@login_required
@never_cache
def displaycourse_fun(request):
    coursedata = Course.objects.all()
    return render(request, "displaycourse.html", {'data': coursedata})


@login_required
@never_cache
def updatecourse_fun(request, courseid):
    c1 = Course.objects.get(id=courseid)
    if request.method == 'POST':
        c1.course_name = request.POST['txtCourseName']
        c1.course_duration = request.POST['txtCourseDuration']
        c1.course_fees = int(request.POST['txtCourseFees'])
        c1.save()
        return redirect('display_course')
    else:
        return render(request, 'updatecourse.html', {'data': c1})


@login_required
@never_cache
def deletecourse_fun(request, courseid):
    c1 = Course.objects.get(id=courseid)
    c1.delete()
    return redirect("display_course")


@login_required
@never_cache
def addstudent_fun(request):
    if request.method == "POST":
        s1 = Student()
        s1.stud_name = request.POST['txtStudentName']
        s1.stud_phno = int(request.POST['txtStudentNum'])
        s1.stud_email = request.POST['txtStudentMail']
        s1.stud_city = City.objects.get(city_name=request.POST['ddlcity'])
        s1.stud_course = Course.objects.get(course_name=request.POST['ddlcourse'])
        s1.paid_fees = int(request.POST['txtPaidFees'])

        c1 = Course.objects.get(course_name=request.POST['ddlcourse'])
        s1.pending_fees = c1.course_fees - s1.paid_fees
        s1.save()
        return redirect('add_student')
    else:
        city = City.objects.all()
        course = Course.objects.all()
        return render(request, "addstudent.html", {"citydata": city, 'coursedata': course})


@login_required
@never_cache
def displaystudent_fun(request):
    s1 = Student.objects.all()
    return render(request, 'displaystudent.html', {'student': s1})


@login_required
@never_cache
def updatestudent_fun(request, stud_id):
    s1 = Student.objects.get(id=stud_id)
    if request.method == "POST":
        s1.stud_name = request.POST['txtStudentName']
        s1.stud_phno = int(request.POST['txtStudentNum'])
        s1.stud_email = request.POST['txtStudentMail']
        s1.stud_city = City.objects.get(city_name=request.POST['ddlcity'])
        s1.stud_course = Course.objects.get(course_name=request.POST['ddlcourse'])
        s1.paid_fees = s1.paid_fees + int(request.POST['txtPaidFees'])

        c1 = Course.objects.get(course_name=request.POST['ddlcourse'])
        if s1.pending_fees > 0:
            s1.pending_fees = c1.course_fees - s1.paid_fees
        else:
            s1.pending_fees = 0

        s1.save()
        return redirect('displaystudent')
    else:
        city = City.objects.all()
        course = Course.objects.all()
        return render(request, "updatestudent.html", {"student": s1, "citydata": city, 'coursedata': course})


@login_required
@never_cache
def deletestudent_fun(request, stud_id):
    s1 = Student.objects.get(id=stud_id)
    s1.delete()
    return redirect('displaystudent')


@login_required
@never_cache
def logout_fun(request):
    logout(request)
    return redirect("log")
