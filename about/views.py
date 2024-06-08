from django.shortcuts import render
from .models import Faqs


def about(request):
    """ A view to return the index page """

    return render(request, 'about/about.html')


def faqs(request):

    context = {
        'faqs': Faqs.objects.all(),
    }

    return render(request, 'about/faqs.html', context)