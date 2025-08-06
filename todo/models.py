from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    