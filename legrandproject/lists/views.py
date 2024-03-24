from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Rafael. You're at the lists index.")
