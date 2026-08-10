from .models import SaytSozlamalari


def sayt_sozlama(request):
    return {'sayt': SaytSozlamalari.objects.first()}