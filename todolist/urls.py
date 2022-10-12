from django.urls import path
from todolist.views import addTask, check, deleteTask, show_todolist, addTask_ajax, show_json
from todolist.views import register #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import logout_user #sesuaikan dengan nama fungsi yang dibuat

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('json/', show_json, name='show_json'),
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat
    path('create-task/', addTask, name='create-task'),
    path('check/<int:pk>/', check, name='check'),
    path('deleteTask/<int:pk>/', deleteTask, name='deleteTask'),
    path('json/', show_json, name='show_json'),
    path('addTask_ajax/', addTask_ajax, name='addTask_ajax'),
]

