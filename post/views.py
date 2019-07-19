from django.shortcuts import render,get_object_or_404,redirect
from .models import Post, Author
from .forms import PostModelForm

# Create your views here
def posts_list(request):
    all_posts = Post.objects.all()
    context = {
        'all_posts':all_posts
    }
    return render(request, "posts/post_list.html", context)


def post_details(request, slug):
    unique_post = get_object_or_404(Post, slug=slug)
    context = {
        'post': unique_post
    }
    return render(request, "posts/post_details.html", context)


def post_create(request):
    author, created = Author.objects.get_or_create(
        user=request.user,
        email= request.user.email,
        cellphone_num=9439439
    )
    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.author = author
        form.save()
        return redirect('/post/')

    context = {
        'form': form
    }
    return render(request, "posts/post_create.html", context)



def post_update(request,slug):
    unique_post = get_object_or_404(Post,slug=slug)
    form = PostModelForm(request.POST or None,
                         request.FILES or None,
                         instance=unique_post)
    if form.is_valid():
        form.save() ##push the update on db
        return redirect('/post/')
    context={
        'form':form
    }
    return render(request, "posts/post_create.html", context)


def post_delete(request, slug):
    unique_post = get_object_or_404(Post,slug=slug)
    unique_post.delete()
    return redirect('/post')