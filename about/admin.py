from django.contrib import admin
from .models import Faqs, AboutUs
from .forms import AboutUsForm


class AboutUsAdmin(admin.ModelAdmin):
    form = AboutUsForm

    def has_add_permission(self, request):
        # Allow adding only if there is no instance
        if AboutUs.objects.exists():
            return False
        return True


admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Faqs)
