from django.shortcuts import render

from .models import Material


def materiallar_royxati(request):
    """Barcha materiallar. Filtrlash brauzerda (JS) bajariladi, URL'dagi
    ?til= va ?turi= parametrlari faqat boshlang'ich faol tabni belgilaydi."""
    materiallar = Material.objects.all()

    tanlangan_til = request.GET.get('til', '')
    tanlangan_tur = request.GET.get('turi', '')

    # Noto'g'ri parametr kelsa "barchasi" holatiga qaytamiz
    if tanlangan_til not in dict(Material.TIL_TANLOVLARI):
        tanlangan_til = ''
    if tanlangan_tur not in dict(Material.TUR_TANLOVLARI):
        tanlangan_tur = ''

    return render(request, 'materials/materials.html', {
        'materiallar': materiallar,
        'til_tanlovlari': Material.TIL_TANLOVLARI,
        'tur_tanlovlari': Material.TUR_TANLOVLARI,
        'tanlangan_til': tanlangan_til,
        'tanlangan_tur': tanlangan_tur,
    })
