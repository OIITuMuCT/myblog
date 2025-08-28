from django.urls import path

from blog import views

urlpatterns = [
    path('hello-world/', views.basic_req),
    path('hello-world-2/', views.basic_req_2),
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('view/', views.blog_view)
]
