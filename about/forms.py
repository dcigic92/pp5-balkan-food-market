from django import forms
from .models import Faqs, AboutUs
from django.core.exceptions import ValidationError


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faqs
        fields = ['question', 'answer']


class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = '__all__'

    def clean(self):
        if not self.instance.pk and AboutUs.objects.exists():
            raise ValidationError('There can only be one About Us instance in the database.')
        return super().clean()