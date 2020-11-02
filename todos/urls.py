from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.list_todo_items),
    path('insert_todo/', views.insert_todo_item, name='insert_todo_item'),
    path('delete/<int:pk>', views.delete_todo_item, name='delete_todo_item')
]
