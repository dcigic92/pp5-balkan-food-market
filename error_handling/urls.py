from django.urls import path
from django.conf.urls import handler404, handler500
from error_handling.views import error_404_view, error_500_view

handler404 = error_404_view
handler500 = error_500_view

urlpatterns = []