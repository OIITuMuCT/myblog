from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from rest_framework import views
from rest_framework import generics
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from blog.serializers import BlogSerializer
from blog.models import Blog


class BlogGetCreateView(views.APIView):
    """List of Blogs"""

    def get(self, request):
        blog_obj_list = Blog.objects.all()
        blogs = BlogSerializer(blog_obj_list, many=True)
        return Response(blogs.data)

    def post(self, request):
        input_data = request.data
        b_obj = BlogSerializer(data=input_data)
        if b_obj.is_valid():
            b_obj.save()
            return Response(b_obj.data, status=status.HTTP_201_CREATED)
        return Response(b_obj.errors, status=status.HTTP_400_BAD_REQUEST)  


class BlogListView(ListView):
    model = Blog
    template_name = "blog_list.html"


class BlogGetUpdateView(generics.ListCreateAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        blogs_queryset = Blog.objects.filter(id__gt=1)
        return blogs_queryset


class BlogGetUpdateFilterView(generics.ListAPIView):
    serializer_class = BlogSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["title"]


def update_blog_title(request):
    blog_id = request.GET.get("id")
    blog = Blog.objects.get(id=blog_id)
    if request.user.has_perm("blog.update_title"):
        return HttpResponse("User has permission to update title")
    return HttpResponse("User does not have permission to update title")


def check_permission(user, group_name):
    return user.groups.filter(name=group_name).exists()


@api_view(["POST"])
def blog_view(request):
    if not check_permission(request.user, "can_view_blog"):
        return Response(status=403)
    # perform operation


@api_view(["GET"])
def basic_req(request):
    if request.method == "GET":
        resp = {"msg": "hello world!"}
        return Response(data=resp, status=status.HTTP_200_OK)


@api_view(["GET"])
def basic_req_2(request):
    if request.method == "GET":
        resp = {"msg": "hello world!"}
        return Response(data=resp, status=status.HTTP_200_OK)
