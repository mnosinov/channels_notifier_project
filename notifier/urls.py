from django.urls import path
from .views import index, status_form

urlpatterns = [
    path('', index),
    path('status/', status_form, name="status"),
]
