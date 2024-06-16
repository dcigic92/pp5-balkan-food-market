from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us, name='about_us'),
    path('edit/', views.edit_about_us, name='edit_about_us'),
    path('create/', views.create_about_us, name='create_about_us'),
    path('delete/', views.delete_about_us, name='delete_about_us'),
    path('faqs/', views.faq_list, name='faq_list'),
    path('faqs/new/', views.faq_create, name='faq_create'),
    path('faqs/edit/<int:pk>/', views.faq_edit, name='faq_edit'),
    path('faqs/delete/<int:pk>/', views.faq_delete, name='faq_delete'),
]
