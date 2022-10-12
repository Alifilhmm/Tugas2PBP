
# Create your views here.
import imp
from django.shortcuts import render
from todolist.models import ToDoList
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from todolist.models import ToDoList
from .forms import create_form
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = ToDoList.objects.filter(user=request.user)
    context = {
        'todolist': data_todolist,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def show_json(request):
    data_todolist = ToDoList.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', data_todolist), content_type='application/json')


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response  
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def deleteTask(request, pk):
    item = ToDoList.objects.filter(pk=pk)
    item.delete()
    return redirect('todolist:show_todolist')

def addTask(request):

    if request.method == "POST":
        form = create_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            ToDoList.objects.create(title = title, description = description, date = datetime.datetime.now(), user = request.user)
            return redirect('todolist:show_todolist')
    else: 
        form = create_form()

    context = {
        'form' : form,
        }
    return render(request, "create-task.html", context)

def check(request, pk):

    temp = ToDoList.objects.filter(user=request.user).get(pk=pk)
    if (temp.is_finished == False):
        temp.is_finished = True
    else :
        temp.is_finished = False
    temp.save()
    return redirect('todolist:show_todolist')


@login_required(login_url='/todolist/login/')
@csrf_exempt
def addTask_ajax(request):
    if request.method == 'POST':
        print("i")
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title != "" or description != "":
            task = ToDoList.objects.create(title = title, description = description, date = datetime.datetime.now(), user = request.user)
            context = {
                'pk' : task.pk,
                'fields' : {
                    'title' : task.title,
                    'description' : task.description,
                    'is_finished' : task.is_finished,
                    'date' : task.date
                }
            }
            return JsonResponse(context)




