from django import forms
from django.forms import formset_factory
from .models import ExampleModel


class ExampleForm(forms.ModelForm):
    class Meta:
        model = ExampleModel
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'Имя',
            'email': 'Электронная почта',
            'message': 'Сообщение',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

ExampleFormSet = formset_factory(ExampleForm, extra=3)
