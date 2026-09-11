from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse,Http404
import logging
from .models import Post

# posts=[
#         {'id':1, 'title':'Post 1','content':'Content of Post 1'},
#         {'id':2,  'title':'Post 2','content':'Content of Post 2'},
#         {'id':3,  'title':'Post 3','content':'Content of Post 3'},
#         {'id':4,  'title':'Post 4','content':'Content of Post 4'},
#         {'id':5,  'title':'Post 5','content':'Content of Post 5'},
#         {'id':6,  'title':'Post 6','content':'Content of Post 6'}
#     ]
posts = Post.objects.all().values("id", "title", "content", "img_url", "created_at")

def login(request):
    return render(request,'blog/login.html')

def index(request):
    blog_title="Latest Posts"
    return render(request,'blog/index.html',{'blog_title':blog_title,'posts':posts})

def detail(request):
    return JsonResponse({
        "message": "Hello world, you are at post detail section",
        "status":"success"
    })

def detailWithId(request,post_id):
    # post=next((item for item in posts if item['id']==post_id),None)
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post Does not Exist!")
    logger=logging.getLogger("Testing")
    logger.debug(f'post variable is {post}')
    return render(request,'blog/detail.html',{'post': post})

def old_url_redirect(request):
    return redirect('new_url_view')

def new_url_view(request):
    return HttpResponse("You are redirected!")