from django.shortcuts import render
from .forms import ExampleFormSet
from django.http import HttpResponse
# Create your views here.


def handle_formset(request):
    if request.method == 'POST':
        formset = ExampleFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                form.save()
            return HttpResponse("Данные успешно сохранены!")
        else:
            return render(request, 'formset_page.html', {'formset': formset})
    else:
        formset = ExampleFormSet()
    return render(request, 'formset_page.html', {'formset': formset})
