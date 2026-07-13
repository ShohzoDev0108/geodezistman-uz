from django.db import models


class EquipmentCategory(models.Model):
    nomi = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Uskuna kategoriyasi"
        verbose_name_plural = "Uskuna kategoriyalari"

    def __str__(self):
        return self.nomi


class Equipment(models.Model):
    nomi = models.CharField(max_length=200)
    kategoriya = models.ForeignKey(
        EquipmentCategory, on_delete=models.CASCADE, related_name='uskunalar'
    )
    tavsifi = models.TextField(blank=True)
    rasm = models.ImageField(upload_to='equipment/', blank=True, null=True)
    narxi_diapazoni = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nomi
