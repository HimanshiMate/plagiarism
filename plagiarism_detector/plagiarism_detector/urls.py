from django.urls import path
from . import views

urlpatterns = [
    path('api/detect-text/', views.detect_text, name='detect_text'),
    path('api/detect-pdf/', views.detect_pdf, name='detect_pdf'),
    path('api/detect-image/', views.detect_image, name='detect_image'),
]
