from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def home(request):
    task = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'ToDo/index.html',{'task':task, 'form':form})

def update(request,id):
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')


    return render(request, 'ToDo/update.html',{'task':task, 'form':form})


def delete(request, id):
    task = Task.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request, 'ToDo/delete.html', {'task':task})
