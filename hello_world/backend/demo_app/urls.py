from django.urls import path

from demo_app import views

##To get all blogs
# * Avoid GET /get-all-blogs, rather use GET /blogs
## To delete a particular blog
# * Avoid POST /delete-blog rather use DELETE /blogs/<blogId>
##To create a new blog with POST request
# * Avoid POST /create-new-blog rather use POST /blogs
##To update an existing blog with a PUT request
# * Avoid PUT /update-blog rather use PUT /blogs/<blogId>

urlpatterns = [
    path("hello-world/", views.hello_world),
    # This is the new line we added for "Linking app views using urls.py" section
    path("hello-world-drf/", views.hello_world_drf),
    # Next 3 line we added for "Use API Versioning" section
    path('demo-version/', views.demo_version),
    path('custom-version/', views.DemoView.as_view()),
    path('another-custom-version/', views.AnotherView.as_view()),
]
