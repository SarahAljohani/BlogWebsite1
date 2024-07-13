
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.users, name='users'),
    path('categories/', views.categories, name='categories'),
    path('blogs/', views.blogs, name='blogs'),
    path('comments/', views.comments, name='comments'),
    path('blogs/<int:id>/', views.blog_details, name='blog_details'),
]



