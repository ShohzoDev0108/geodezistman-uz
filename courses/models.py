from django.db import models


class CourseCategory(models.Model):
    nomi = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Kurs kategoriyasi"
        verbose_name_plural = "Kurs kategoriyalari"

    def __str__(self):
        return self.nomi


class Course(models.Model):
    nomi = models.CharField(max_length=200)
    kategoriya = models.ForeignKey(
        CourseCategory, on_delete=models.CASCADE, related_name='kurslar'
    )
    tavsifi = models.TextField()
    muqova_rasm = models.ImageField(upload_to='course_covers/', blank=True, null=True)
    yaratilgan_sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi


class Lesson(models.Model):
    kurs = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='darslar')
    sarlavha = models.CharField(max_length=200)
    matn = models.TextField(blank=True)
    video_link = models.URLField(blank=True, null=True)
    tartib_raqami = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['tartib_raqami']

    def __str__(self):
        return f"{self.kurs.nomi} — {self.sarlavha}"

class SaytSozlamalari(models.Model):
    email = models.EmailField(blank=True)
    telegram = models.CharField(max_length=100, blank=True, help_text="Masalan: @geodezistman")
    manzil = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Sayt sozlamalari"
        verbose_name_plural = "Sayt sozlamalari"

    def __str__(self):
        return "Sayt sozlamalari"
