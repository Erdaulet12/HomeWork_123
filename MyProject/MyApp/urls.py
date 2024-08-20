from django.urls import path
from .views import task_list, task_detail, TaskCreate, TaskDelete

urlpatterns = [
    path('tasks/', task_list, name='task_list'),
    path('tasks/<int:pk>/', task_detail, name='task_detail'),
    path('tasks/create/', TaskCreate.as_view(), name='task_create'),
    path('tasks/delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
]
