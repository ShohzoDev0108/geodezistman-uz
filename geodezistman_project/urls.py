from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('materiallar/', include('materials.urls')),
    path('uskunalar/', include('equipment.urls')),
    # Statik sahifalar — alohida app talab qilmaydi
    path('biz-haqimizda/',
         TemplateView.as_view(template_name='pages/about.html'),
         name='biz_haqimizda'),
    path('boglanish/',
         TemplateView.as_view(template_name='pages/contact.html'),
         name='boglanish'),
    path('', include('courses.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
