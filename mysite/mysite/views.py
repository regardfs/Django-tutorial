# -*- coding: utf-8 -*-

from django.http import HttpResponse


def helloworld(request):
    return HttpResponse('My first site writen by Django engine, 我的第一个Django网站')