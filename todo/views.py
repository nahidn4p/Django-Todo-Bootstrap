from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate ,logout
from django.contrib.auth.models import User
from django.contrib import messages
from todo.models import TodoItem

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'Account created successfully!')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
            
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('todo')  # Redirect to a todo list page
    return render(request, 'login.html')


def todo_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            todo_item = TodoItem(title=title, user=request.user)
            todo_item.save()
            messages.success(request, 'Todo item added successfully!')
    
    todos = TodoItem.objects.filter(user=request.user)
    return render(request, 'todo.html',{'todos': todos})

def signout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

def delete_todo(request, todo_id):
    if not request.user.is_authenticated:
        return redirect('todo')
    
    try:
        todo_item = TodoItem.objects.get(id=todo_id, user=request.user)
        todo_item.delete()
        messages.success(request, 'Todo item deleted successfully!')
    except TodoItem.DoesNotExist:
        messages.error(request, 'Todo item does not exist.')
    
    return redirect('todo')


def edit_todo(request, todo_id):
    if not request.user.is_authenticated:
        return redirect('todo')
    
    try:
        todo_item = TodoItem.objects.get(id=todo_id, user=request.user)
        if request.method == 'POST':
            title = request.POST.get('title')
            if title:
                todo_item.title = title
                todo_item.save()
                messages.success(request, 'Todo item updated successfully!')
                return redirect('todo')
        return render(request, 'edit_todo.html', {'todo': todo_item})
    except TodoItem.DoesNotExist:
        messages.error(request, 'Todo item does not exist.')
        return redirect('todo')
