from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    task_data = [{"id": task.id, "title": task.title, "description": task.description, "is_completed": task.is_completed} for task in tasks]
    return JsonResponse(task_data, safe=False)


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task_data = {"id": task.id, "title": task.title, "description": task.description, "is_completed": task.is_completed}
    return JsonResponse(task_data)
