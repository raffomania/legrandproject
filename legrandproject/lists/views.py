from django.shortcuts import render

from .models import TodoList    

def index(request):
    latest_lists = TodoList.objects.order_by('title')
    # stuff we put in template
    context = {"latest_list": latest_lists}
    return render(request, "lists/index.html", context)

