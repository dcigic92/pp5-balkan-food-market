from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('faqs/', views.faqs, name='faqs'),
    path('faqs/new/', views.faq_create, name='faq_create'),
    path('faqs/edit/<int:pk>/', views.faq_edit, name='faq_edit'),
    path('faqs/delete/<int:pk>/', views.faq_delete, name='faq_delete'),
]
