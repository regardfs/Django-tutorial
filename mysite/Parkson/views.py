# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect

from django.template.defaulttags import register

from Parkson.models import Parkson, Food, Comment
from Parkson.forms import CommentForm
import datetime

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def helloworld(request):
    return HttpResponse('My first site writen by Django engine, 我的第一个Django网站')


def math(request, a, b):
    a = float(a)
    b = float(b)
    s = a + b
    d = a - b
    p = a * b
    q = a / b
    return render_to_response('math.html',locals())


def PizzaHut(request):
    pizza_1 = {'name': '芝士鸡肉披萨', 'numbers': 1, 'price': 59, 'is_spicy': '1', 'favourite': True}
    pizza_2 = {'name': '鸡翅', 'numbers': 2, 'price': 14, 'is_spicy': '0', 'favourite': True}
    pungency_degree = {'0': '不辣', '1': '微辣', '2': '中辣', '3': ' 非常辣'}
    foods = [pizza_1, pizza_2]
    return render_to_response('menu.html',locals())


def menu(request):
    restaurants = Parkson.objects.all()
    return render_to_response('parkson.html',locals())


def restaurants_list(request):
    restaurants = Parkson.objects.all()
    return render_to_response('restaurants_list.html', locals())


def restaurants_list1(request):
    restaurants = Parkson.objects.all()
    return render_to_response('restaurants_list1.html', locals())


def menu1(request, id):
    if 'id':
        r = Parkson.objects.get(id=id)
        return render_to_response('menu1.html',locals())
    else:
        return HttpResponseRedirect("/restaurants_list1/")


def menu2(request, id):
    if 'id':
        r = Parkson.objects.get(id=id)
        return render_to_response('menu1.html',locals())
    else:
        return HttpResponseRedirect("/restaurants_list1/")


def comment(request,id):
    if id:
        r = Parkson.objects.get(id=id)
    else:
        return HttpResponseRedirect("/restaurants_list/")
    if 'ok' in request.POST:
        f = CommentForm(request.POST)
        if f.is_valid():
            user = f.cleaned_data['user']
            content = f.cleaned_data['content']
            email = f.cleaned_data['email']
            date_time = datetime.datetime.now()
            c = Comment(user=user, email=email, content=content, date_time=date_time, restaurant=r)
            c.save()
            f = CommentForm()
    else:
        f = CommentForm()
    return render_to_response('comments.html',locals())


def comment_as_table(request,id):
    if id:
        r = Parkson.objects.get(id=id)
    else:
        return HttpResponseRedirect("/restaurants_list/")
    if 'ok' in request.POST:
        f = CommentForm(request.POST)
        if f.is_valid():
            user = f.cleaned_data['user']
            content = f.cleaned_data['content']
            email = f.cleaned_data['email']
            date_time = datetime.datetime.now()
            c = Comment(user=user, email=email, content=content, date_time=date_time, restaurant=r)
            c.save()
            f = CommentForm()
    else:
        f = CommentForm()
    return render_to_response('comments_as_table.html',locals())