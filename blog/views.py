from django.shortcuts import render, redirect
from .models import Post
from blog.forms import CommentForm


def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'post_list' : post_list,
    })

def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post' : post,
    })

def comment_new(request, post_pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=post_pk)
            comment.save()
            return redirect('blog:post_detail',post_pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form':form})


# Create your views here.
