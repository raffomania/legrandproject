from django.db import models


class TodoList(models.Model):
    title = models.CharField(max_length=200)

class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    done = models.BooleanField()
    edit_date = models.DateTimeField('edit date')
    parent_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
