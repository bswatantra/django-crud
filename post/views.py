from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html' , {'posts':posts})


def create(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    return HttpResponse('Invalid method', status=404)

def store(request):
    # store data
    if request.method == 'POST':
        pass  # Add this to avoid syntax error
    return HttpResponse('Invalid method', status=404)

def show(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'show.html' , {'post':post})

def edit(request):
    return render(request, 'edit.html')


def update(request):
    # update data
    pass  # Add this to avoid syntax error


def destroy(request):
    # update data
    pass  # Add this to avoid syntax error