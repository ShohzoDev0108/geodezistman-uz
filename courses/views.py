from django.shortcuts import get_object_or_404, render

from .models import Course, CourseCategory


def home(request):
    return render(request, 'courses/home.html')


def kurslar_royxati(request):
    kurslar = Course.objects.select_related('kategoriya')
    return render(request, 'courses/courses.html', {'kurslar': kurslar})


def kurs_detali(request, pk):
    """Bitta kurs va uning darslari (tartib_raqami bo'yicha saralangan)."""
    kurs = get_object_or_404(Course.objects.select_related('kategoriya'), pk=pk)
    darslar = kurs.darslar.order_by('tartib_raqami', 'id')
    return render(request, 'courses/course_detail.html', {
        'kurs': kurs,
        'darslar': darslar,
    })
