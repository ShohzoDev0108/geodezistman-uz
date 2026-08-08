from django.shortcuts import get_object_or_404, render

from .models import Course, CourseCategory


def home(request):
    return render(request, 'courses/home.html')


def kurslar_royxati(request):
    """Barcha kurslar. Navbar dropdown'i ?kategoriya=<slug> orqali filtrlaydi;
    noma'lum slug kelsa barcha kurslar ko'rsatiladi."""
    kurslar = Course.objects.select_related('kategoriya')

    kategoriya_slug = request.GET.get('kategoriya', '')
    tanlangan_kategoriya = None
    if kategoriya_slug:
        tanlangan_kategoriya = CourseCategory.objects.filter(slug=kategoriya_slug).first()
        if tanlangan_kategoriya is not None:
            kurslar = kurslar.filter(kategoriya=tanlangan_kategoriya)

    return render(request, 'courses/courses.html', {
        'kurslar': kurslar,
        'tanlangan_kategoriya': tanlangan_kategoriya,
    })


def kurs_detali(request, pk):
    """Bitta kurs va uning darslari (tartib_raqami bo'yicha saralangan)."""
    kurs = get_object_or_404(Course.objects.select_related('kategoriya'), pk=pk)
    darslar = kurs.darslar.order_by('tartib_raqami', 'id')
    return render(request, 'courses/course_detail.html', {
        'kurs': kurs,
        'darslar': darslar,
    })
