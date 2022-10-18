from tkinter.messagebox import NO
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def add(request):
    form = StudentForm(request.POST or None)
    #student = Student.objects.all()
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'add.html', {'form':form})
def show(request):
    student = Student.objects.all()
    return render(request, 'show.html', {'student':student})
def update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'update.html', {'student':student})
def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return HttpResponseRedirect('/')
