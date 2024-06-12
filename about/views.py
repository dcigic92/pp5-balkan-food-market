from django.shortcuts import render, get_object_or_404, redirect
from .models import Faqs
from .forms import FaqForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def about(request):
    """ A view to return about page """

    return render(request, 'about/about.html')


def faqs(request):
    """ A view to return FAQs page """

    context = {
        'faqs': Faqs.objects.all(),
    }

    return render(request, 'about/faqs.html', context)


@login_required
def faq_create(request):
    """ Create a new FAQ """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do that.')
        return redirect('faqs')
    
    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added FAQ!')
            return redirect('faqs')
        else:
            messages.error(request, 'Failed to add FAQ. Please ensure the form is valid.')
    else:
        form = FaqForm()
    return render(request, 'about/faq_form.html', {'form': form})


@login_required
def faq_edit(request, pk):
    """ Edit an existing FAQ """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do that.')
        return redirect('faqs')
    
    faq = get_object_or_404(Faqs, pk=pk)
    if request.method == 'POST':
        form = FaqForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited FAQ!')
            return redirect('faqs')
        else:
            messages.error(request, 'Failed to edit FAQ. Please ensure the form is valid.')
    else:
        form = FaqForm(instance=faq)
    return render(request, 'about/faq_form.html', {'form': form})


@login_required
def faq_delete(request, pk):
    """ Delete an existing FAQ """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do that.')
        return redirect('faqs')
    
    faq = get_object_or_404(Faqs, pk=pk)
    faq.delete()
    messages.success(request, 'FAQ deleted!')
    return redirect('faqs')