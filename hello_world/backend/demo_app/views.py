from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


def hello_world(request):
    return HttpResponse('hello world')


@api_view(["GET"])
def hello_world_drf(request, *args, **kwargs):
    return Response(data={"msg": "hello world"})

@api_view(['GET'])
def demo_version(request, *args, **kwargs):
    version = request.version
    return Response(data={
        'msg': f'You have hit {version} of demo-api'
    })
