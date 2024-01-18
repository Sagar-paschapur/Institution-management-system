from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=150)
    course_duration = models.CharField(max_length=150)
    course_fees = models.IntegerField()

    def __str__(self):
        return (f"{self.course_name}")

class City(models.Model):
    city_name = models.CharField(max_length=150)

    def __str__(self):
        return (f"{self.city_name}")

class Student(models.Model):
    stud_name = models.CharField(max_length=150)
    stud_phno = models.BigIntegerField()
    stud_email = models.CharField(max_length=100)
    paid_fees = models.IntegerField()
    pending_fees = models.IntegerField()
    stud_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    stud_city = models.ForeignKey(City, on_delete= models.CASCADE)