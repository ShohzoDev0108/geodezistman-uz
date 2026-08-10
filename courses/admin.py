from django.contrib import admin
from .models import CourseCategory, Course, Lesson, SaytSozlamalari


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'slug']
    prepopulated_fields = {'slug': ('nomi',)}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'kategoriya', 'yaratilgan_sana']
    list_filter = ['kategoriya']
    search_fields = ['nomi']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['sarlavha', 'kurs', 'tartib_raqami']
    list_filter = ['kurs']

@admin.register(SaytSozlamalari)
class SaytSozlamalariAdmin(admin.ModelAdmin):
    list_display = ['email', 'telegram', 'manzil']