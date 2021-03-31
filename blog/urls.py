from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list,name="post_list"),
    path("<int:pk>/",views.blog_detail,name="blog_detail"),
    path("<category>/",views.blog_category,name="blog_category"),
]
