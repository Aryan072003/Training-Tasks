from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    tasks = Todo.objects.all()
    if request.method == "POST":
        title = request.POST.get('task')
        Todo.objects.create(title = title)
        return redirect('index')
    return render(request, 'mytodo/index.html', {"tasks": tasks})
