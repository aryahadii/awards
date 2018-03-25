from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MessageRegisterForm


def index(request):
    if request.method == 'POST':
        register_form = MessageRegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect('/thanks/')

    else:
        register_form = MessageRegisterForm()

    return render(request, 'index.html', {'form': register_form})


def thanks(request):
    return render(request, 'thanks.html')
