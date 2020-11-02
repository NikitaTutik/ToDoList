from django.shortcuts import render, redirect
from .models import Todo


def list_todo_items(request):
    content = {'todos': Todo.objects.all()}
    return render(request, 'todos/todo_list.html', content)


def insert_todo_item(request):
    todo = Todo(content=request.POST['content'])
    todo.save()
    return redirect('/todos/list/')


def delete_todo_item(request, pk):
    todo_delete = Todo.objects.get(id=pk)
    todo_delete.delete()
    return redirect('/todos/list/')
