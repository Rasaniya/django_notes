from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Notes
from .forms import newNote
# Create your views here.

def index(request):
    notes = Notes.objects.all()
    context = {'notes':notes}
    return render(request, 'index.html', context)

def new(request):
    form = newNote()
    if request.method == 'POST':
        form = newNote(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/notes')
    
    context = {'form':form}
    return render(request, 'new.html', context)            