from django.urls import path
from hello import views

app_name = 'hello'

urlpatterns = [
    path('say_hello', views.say_hello, name='say_hello'),
    path('post_list', views.post_list, name='post_list'),
    path('post_detail/<int:pk>', views.post_detail, name="post_detail"),
    path('post_new', views.post_new, name="post_new"),
    path('post_detail/<int:pk>/edit', views.post_edit, name="post_edit"),
]