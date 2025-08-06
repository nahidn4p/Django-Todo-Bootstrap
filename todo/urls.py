from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('', views.login_view, name='login'),
    path('todo/', views.todo_list, name='todo'),
    path('signout/', views.signout, name='signout'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('edit_todo/<int:todo_id>/', views.edit_todo, name='edit_todo'),
]
