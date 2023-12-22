from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts': posts})

def post(request,pk):
    posts = Post.objects.get(id = pk)
    return render(request,'post.html',{'posts': posts})

from .forms import PostForm

def add_blog_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Save the form and get the instance of the model
            post = form.save(commit=False)
            # Assign the current user as the author
            post.author = request.user.username
            post.save()
            # Redirect to the blog home page after adding a post
            return redirect('/')
    else:
        form = PostForm()

    return render(request, 'add_post.html', {'form': form, 'username': request.user.username})

def login(request):
    return redirect('/admin')
    