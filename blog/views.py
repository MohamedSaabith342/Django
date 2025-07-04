from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse
from django.urls import reverse
import logging

from .models import Post



# posts = [
#     {'id':1,'title':'post 1','content':'Content of post 1'},
#     {'id':2,'title':'post 2','content':'Content of post 2'},
#     {'id':3,'title':'post 3','content':'Content of post 3'},
#     {'id':4,'title':'post 4','content':'Content of post 4'},
#   ]
# Create your views here.
def index(request):
  blog_title = 'Latest Posts'
  posts=Post.objects.all()
  
  return render(request,'blog/index.html',{'blog_title':blog_title,'posts':posts})

def detail(request,slug):
  # post = next((item for item in posts if item['id'] == int(post_id)),None)
  # logger = logging.getLogger("TESTING")
  # logger.debug(f'post variable is {post}')
    try:

     post = Post.objects.get(slug=slug)

    except Post.DoesNotExist:
      raise Http404("Please Does Not Exist!")
    return render(request,'blog/detail.html',{'post':post})


def old_url_redirect(request):
  return redirect(reverse('blog:new_page_url'))


def new_url_view(request):
  return HttpResponse ("This is the new url")