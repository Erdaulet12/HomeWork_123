from django.shortcuts import render
from django.http import JsonResponse
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    task_data = [{"id": task.id, "title": task.title, "description": task.description, "is_completed": task.is_completed} for task in tasks]
    return JsonResponse(task_data, safe=False)
