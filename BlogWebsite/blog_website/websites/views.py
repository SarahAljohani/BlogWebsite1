

from django.http import HttpResponse
from django.template import loader
from .models import User, Category, Post, Comment

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render({}, request))

def users(request):
    users = User.objects.all().values('username', 'email')
    template = loader.get_template('users.html')
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))

def categories(request):
    categories = Category.objects.all().values()
    template = loader.get_template('categories.html')
    context = {
        'categories': categories,
    }
    return HttpResponse(template.render(context, request))

def blogs(request):
    blogs = Post.objects.all().values('id', 'title')
    template = loader.get_template('blogs.html')
    context = {
        'blogs': blogs,
    }
    return HttpResponse(template.render(context, request))

def comments(request):
    comments = Comment.objects.all().values('content', 'post_id')
    template = loader.get_template('comments.html')
    context = {
        'comments': comments,
    }
    return HttpResponse(template.render(context, request))

def blog_details(request, id):
    blog = Post.objects.get(id=id)
    template = loader.get_template('blogdetails.html')
    context = {
        'blog': blog,
    }
    return HttpResponse(template.render(context, request))