from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo

def index(request):
    # Get all todos ordered by creation date in descending order
    todo_list = Todo.objects.order_by('-created_at')
    
    # Render the 'index.html' template with the list of todos
    return render(request, 'todos/index.html', {'todo_list': todo_list})

def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        Todo.objects.create(title=title)
        return redirect('todos:index')
    else:
        return render(request, 'todos/add.html')

def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return redirect('todos:index')

def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    todo.isCompleted = isCompleted
    todo.save()
    return redirect('todos:index')
