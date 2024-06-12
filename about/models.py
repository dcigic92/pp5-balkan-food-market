from django.db import models
from django.core.exceptions import ValidationError


class Faqs(models.Model):
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        verbose_name = "FAQs"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question
    

class AboutUs(models.Model):
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.pk and AboutUs.objects.exists():
            raise ValidationError('There can only be one About Us instance in the database.')
        super(AboutUs, self).save(*args, **kwargs)

    def __str__(self):
        return "About Us"

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"