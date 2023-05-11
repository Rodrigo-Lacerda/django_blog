from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import ListView, UpdateView

from .models import Post as modelPost

# Create your views here.
class Post(DetailView):
    model = modelPost



class PostList(ListView):
    model = modelPost



class PostUpdate(UpdateView):
    model = modelPost
    fields = ["content"]
    template_name_suffix = "_update_form"

