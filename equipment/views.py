from django.shortcuts import render
from django.utils.text import slugify

from .models import EquipmentCategory


def uskunalar_royxati(request):
    """Uskunalar kategoriya bo'yicha guruhlab ko'rsatiladi. Filtrlash brauzerda
    (JS) bajariladi, URL'dagi ?kategoriya=<slug> boshlang'ich tanlovni belgilaydi."""
    kategoriyalar = (
        EquipmentCategory.objects
        .prefetch_related('uskunalar')
        .order_by('nomi')
    )

    # Har bir kategoriya uchun slug — filtr tugmalari va URL parametri shu asosda
    guruhlar = [
        {
            'nomi': kategoriya.nomi,
            'slug': slugify(kategoriya.nomi),
            'uskunalar': list(kategoriya.uskunalar.all()),
        }
        for kategoriya in kategoriyalar
    ]
    guruhlar = [guruh for guruh in guruhlar if guruh['uskunalar']]

    tanlangan_kategoriya = request.GET.get('kategoriya', '')
    if tanlangan_kategoriya not in {guruh['slug'] for guruh in guruhlar}:
        tanlangan_kategoriya = ''

    return render(request, 'equipment/equipment.html', {
        'guruhlar': guruhlar,
        'tanlangan_kategoriya': tanlangan_kategoriya,
    })
