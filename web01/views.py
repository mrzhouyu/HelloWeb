# -*-coding:utf-8 -*-
from django.shortcuts import render,redirect
from web01.models import Post
from django.http import HttpResponse
from datetime import datetime
from django.template.loader import get_template

# Create your views here.
#读取所有内容到网页
def read(request):
    template = get_template('index.html')
    posts=Post.objects.all()
    now=datetime.now()
    html=template.render(locals())
    return HttpResponse(html)
def body(request,slug):
    template=get_template('post.html')
    try:
        post=Post.objects.get(slug=slug)
        if post!=None:
            html=template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')


