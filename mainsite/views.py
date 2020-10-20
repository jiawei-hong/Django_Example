from django.shortcuts import render
from .models import Post
import datetime

# Create your views here.
def home(request):
    return render(request,'index.html',{
        'test':'xxx'
    })

def create(request):
    return render(request,'index.html',{
        'test': Post.objects.create(title='xxx',slug='test_slug',body='test_body').id
    })

def index(request):
    return render(request,'index.html',{
        'post_instance':Post.objects.all()
    })

def get_time(request):
    return render(request,'index.html',{
        'time': datetime.datetime.now
    })