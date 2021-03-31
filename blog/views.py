from django.shortcuts import render
from blog.models import Post,Comment
from .form import CommentForm

# Referance from https://realpython.com/get-started-with-django-1/
# Create your views here.
# blog_index will display a list of your posts
# blog _index replace with post_list.
def post_list(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts":posts,
    }
    return render(request,"blog/post.html",context)

#blog_detail will display the full post as well as comments and a form to allow users to create new comments.
#blog_category will be similar to blog_index, but the posts viewed will only be of a specific category chosen by the user.

def blog_category(request,category):
    posts = Post.objects.filter( categories__name__contains=category).order_by('-created_on')
    context = {
        "category":category,
        "posts":posts,
    }
    return render(request,"blog/category.html",context)

def blog_detail(request,pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post = post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {
        "post":post,
        "comments":comments,
        "form":form,
    }
    return render(request,"blog/detail.html",context)
