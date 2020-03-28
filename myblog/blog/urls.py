from django.urls import path
from .views import Add_Blog, Update_Blog, Delete_Blog
from . import views

urlpatterns = [
    path('new/', Add_Blog.as_view(), name='blog-create'),
    path('<int:pk>/update/', Update_Blog.as_view(), name='blog-update'),
    path('<int:pk>/delete/', Delete_Blog.as_view(), name='blog-delete'), 
  #  path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

