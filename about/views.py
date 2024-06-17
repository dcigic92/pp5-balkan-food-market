from django.shortcuts import render, get_object_or_404, redirect
from .models import Faqs, AboutUs
from .forms import FaqForm, AboutUsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def about_us(request):
    """ A view to return About Us page """

    about = AboutUs.objects.first()
    return render(request, 'about/about_us.html', {'about': about})


@login_required
def create_about_us(request):
    """ Create about us"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do that.')
        return redirect('about_us')
    
    if AboutUs.objects.exists():
        messages.error(request, 'Only one About Us instance is allowed.')
        return redirect('about_us')
    
    if request.method == 'POST':
        form = AboutUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'About Us content created successfully.')
            return redirect('about_us')
        else:
            messages.error(request, 'Failed to create About Us. Please ensure the form is valid.')
    else:
        form = AboutUsForm()
    return render(request, 'about/about_us_form.html', {'form': form, 'is_edit': False})


@login_required
def edit_about_us(request):
    """ Edit about us"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do that.')
        return redirect('about_us')
    
    about = get_object_or_404(AboutUs)
    if request.method == 'POST':
        form = AboutUsForm(request.POST, instance=about)
        if form.is_valid():
            form.save()
            messages.success(request, 'About Us content updated successfully.')
            return redirect('about_us')
        else:
            messages.error(request, 'Failed to edit About Us. Please ensure the form is valid.')
    else:
        form = AboutUsForm(instance=about)
    return render(request, 'about/about_us_form.html', {'form': form, 'is_edit': True})


@login_required
def delete_about_us(request):
    """ Delete about us"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do that.')
        return redirect('about_us')
    
    about = get_object_or_404(AboutUs)
    about.delete()
    messages.success(request, 'About Us content deleted successfully.')
    return redirect('about_us')


def faq_list(request):
    """ A view to return FAQs page """

    faqs = Faqs.objects.all()
    return render(request, 'about/faq_list.html', {'faqs': faqs})


@login_required
def faq_create(request):
    """ Create a new FAQ """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do that.')
        return redirect('faq_list')
    
    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added FAQ!')
            return redirect('faq_list')
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
        return redirect('faq_list')
    
    faq = get_object_or_404(Faqs, pk=pk)
    if request.method == 'POST':
        form = FaqForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited FAQ!')
            return redirect('faq_list')
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
        return redirect('faq_list')
    
    faq = get_object_or_404(Faqs, pk=pk)
    faq.delete()
    messages.success(request, 'FAQ deleted successfully.')
    return redirect('faq_list')