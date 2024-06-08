from django.db import models


class Faqs(models.Model):
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question