from django.urls import path
from . import views


app_name = 'todos'

urlpatterns = [
    path('', views.home_page, name='index'),
    path('about/', views.about_page, name='about'),
    path('complete/<int:todo_id>/', views.complete_todo, name='complete'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete'),
    path('delete-completed/', views.delete_completed, name='delete-completed'),
    path('delete/', views.delete_all, name='delete-all'),
]
