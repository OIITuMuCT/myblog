from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request, *args, **kwargs):
    return HttpResponse('hello world')
