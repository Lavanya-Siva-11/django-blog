from django.urls import path
from django.shortcuts import redirect
from . import views

def redirect_to_index(request, any_path=None):
    return redirect("login")

urlpatterns=[
   path("",views.index,name="index1"),
   path("login/",views.login,name="login"),
   path("post/",views.detail,name="detail"),
   path("post/<str:slug>",views.detailWithId,name="detailWithId"),
   path("old_url/",views.old_url_redirect,name="old_url"),
   path("new_url/",views.new_url_view,name="new_url_view"),
   path("contact/",views.contact,name="contact"),
   path("about/",views.about,name="about"),


   path("<path:any_path>", redirect_to_index, name="catch_all"),
]