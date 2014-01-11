import sys
import facebook
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from posts.models import Post
from posts.forms import PostForm

def index(request, error_msg=None):
    posts = Post.objects.all()
    new_post = Post()
    form = PostForm()
    context = {
        'posts': posts,
        'new_post': new_post,
        'post_form': form,
        'error_msg': error_msg,
    }
  
    return render(request, 'posts/index.html', context)
  
def create(request):
    context = {}
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            context['post'] = form.save(commit=False)
            form.save()
    """
    if 'post' in context:
        return render(request, 'posts/_post.html', context)
    else:
        return HttpResponse()
    """

    return HttpResponseRedirect(reverse('index'))
    
def update(request):
    context = {}
    if request.method == 'POST':
        postID = request.POST.__getitem__('id')
        _msg = request.POST.__getitem__('msg')
        _pubTime = request.POST.__getitem__('pubTime')
  
        posts = Post.objects.select_for_update().filter(pk=postID)
        posts.update(msg=_msg, publishTime=_pubTime)
        context['post'] = posts[0]
    
    if 'post' in context:
        return render(request, 'posts/_sub_post.html', context)
    else:
        return HttpResponse()
  
def destroy(request):
    postID = request.POST.__getitem__('id')
    post = Post.objects.filter(pk=postID)[0]
  
    Post.objects.filter(pk=postID).delete()
  
    return HttpResponse()
