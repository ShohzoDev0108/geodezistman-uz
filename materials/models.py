from django.db import models


class Material(models.Model):

    TIL_TANLOVLARI = [
        ('uz', "O'zbekcha"),
        ('ru', "Ruscha"),
    ]

    TUR_TANLOVLARI = [
        ('kitob', "Kitob/Darslik"),
        ('shablon', "Hujjat namunasi"),
    ]

    nomi = models.CharField(max_length=200)
    til = models.CharField(max_length=2, choices=TIL_TANLOVLARI)
    turi = models.CharField(max_length=10, choices=TUR_TANLOVLARI)
    tavsifi = models.TextField(blank=True)
    fayl = models.FileField(upload_to='materials/')
    muqova_rasm = models.ImageField(upload_to='material_covers/', blank=True, null=True)
    yuklangan_sana = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiallar"
        ordering = ['-yuklangan_sana']

    def __str__(self):
        return self.nomi
