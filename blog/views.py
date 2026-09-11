from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse,Http404
import logging
from .models import Post
from django.core.paginator import Paginator
from .forms  import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# posts=[
#         {'id':1, 'title':'Post 1','content':'Content of Post 1'},
#         {'id':2,  'title':'Post 2','content':'Content of Post 2'},
#         {'id':3,  'title':'Post 3','content':'Content of Post 3'},
#         {'id':4,  'title':'Post 4','content':'Content of Post 4'},
#         {'id':5,  'title':'Post 5','content':'Content of Post 5'},
#         {'id':6,  'title':'Post 6','content':'Content of Post 6'}
#     ]

def login(request):
    return render(request,'blog/login.html')

def index(request):
    blog_title="Latest Posts"
    all_posts = Post.objects.all()
    paginator=Paginator(all_posts,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'blog/index.html',{'blog_title':blog_title,'posts':page_obj})

def detail(request):
    return JsonResponse({
        "message": "Hello world, you are at post detail section",
        "status":"success"
    })

def detailWithId(request,slug):
    # post=next((item for item in posts if item['id']==post_id),None)
    try:
        # post = Post.objects.get(pk=post_id)
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post Does not Exist!")
    logger=logging.getLogger("Testing")
    logger.debug(f'post variable is {post}')
    return render(request,'blog/detail.html',{'post': post,'related_posts':related_posts})

def old_url_redirect(request):
    return redirect('new_url_view')

def new_url_view(request):
    return HttpResponse("You are redirected!")

def contact(request):
    logger = logging.getLogger("Testing")

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            logger.debug(f"post req is {name} {email}")

            send_mail(
                subject=f"New contact form message from {name}",
                message=f"From: {name} <{email}>\n\n{message}",
                from_email=f"{email}",
                recipient_list=['admin@example.com'],
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
        else:
            logger.debug(f"form validation failure: {form.errors}")
    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})