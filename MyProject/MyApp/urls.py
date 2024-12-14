from django.urls import path
from .views import handle_formset

urlpatterns = [
    path('formset/', handle_formset, name='handle_formset'),
]
