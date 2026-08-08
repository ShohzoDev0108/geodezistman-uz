from django.shortcuts import render
from .models import Course, CourseCategory


def home(request):
    return render(request, 'courses/home.html')


def kurslar_royxati(request):
    kurslar = Course.objects.all()
    return render(request, 'courses/courses.html', {'kurslar': kurslar})
