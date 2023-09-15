from django.urls import path
from . import views

urlpatterns = [
    path('create_consultation/', views.create_consultation, name='create_consultation'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
]