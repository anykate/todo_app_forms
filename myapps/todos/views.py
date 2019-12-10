from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm


# Create your views here.
def home_page(request):
    form = TodoForm(request.POST or None)
    todos = Todo.objects.all()

    if request.method == 'POST':
        if form.is_valid():
            if len(form.cleaned_data['title']) > 4:
                form.save()
            return redirect('todos:index')

    return render(request, 'todos/index.html', {
        'todos': todos,
        'form': form,
    })


def about_page(request):
    return render(request, 'todos/about.html', {})


def complete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.is_completed = True
    todo.save()
    return redirect('todos:index')


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('todos:index')


def delete_completed(request):
    todos_completed = Todo.objects.filter(is_completed=True).delete()
    return redirect('todos:index')


def delete_all(request):
    todos = Todo.objects.all().delete()
    return redirect('todos:index')
