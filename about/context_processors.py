from .models import AboutUs


def about_us_context(request):
    return {
        'about': AboutUs.objects.first()
    }