from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Task
from django.views import View
from django.utils.decorators import method_decorator
from django.http import JsonResponse, HttpResponseNotAllowed
import json


def task_list(request):
    tasks = Task.objects.all()
    task_data = [{"id": task.id, "title": task.title, "description": task.description, "is_completed": task.is_completed} for task in tasks]
    return JsonResponse(task_data, safe=False)


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task_data = {"id": task.id, "title": task.title, "description": task.description, "is_completed": task.is_completed}
    return JsonResponse(task_data)


@method_decorator(csrf_exempt, name='dispatch')
class TaskCreate(View):
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        task = Task.objects.create(title=data['title'], description=data.get('description', ''))
        task_data = {"id": task.id, "title": task.title, "description": task.description, "is_completed": task.is_completed}
        return JsonResponse(task_data)


@method_decorator(csrf_exempt, name='dispatch')
class TaskDelete(View):
    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return JsonResponse({"message": "Task deleted successfully"})
