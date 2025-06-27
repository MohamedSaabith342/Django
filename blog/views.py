from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
  return HttpResponse("Hello world,You are at blog index")

def detail(request,post_id):
  return HttpResponse(f"You are viewing post detail page. And ID is {post_id}")


def old_url_redirect(request):
  return redirect(reverse('blog:new_page_url'))


def new_url_view(request):
  return HttpResponse ("This is the new url")