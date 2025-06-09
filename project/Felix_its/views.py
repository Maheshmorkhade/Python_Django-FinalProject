from django.shortcuts import render, redirect, get_object_or_404
from .models import Felixclass
from .forms import FelixForm

def all_felix(request):
    felixs = Felixclass.objects.all()
    return render(request, 'felix/All_felix.html', {'felixs': felixs})

def create_course(request):
    if request.method == 'POST':
        form = FelixForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_felix')
    else:
        form = FelixForm()
    return render(request, 'felix/felix_form.html', {'form': form})

def update_course(request, pk):
    course = get_object_or_404(Felixclass, pk=pk)
    form = FelixForm(request.POST or None, request.FILES or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('all_felix')
    return render(request, 'felix/felix_form.html', {'form': form})

def delete_course(request, pk):
    course = get_object_or_404(Felixclass, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('all_felix')
    return render(request, 'felix/felix_confirm_delete.html', {'course': course})
