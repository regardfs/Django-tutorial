# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response


def welcome(request):
    if 'user_name' in request.GET:
        return HttpResponse('Welcome!~'+request.GET['user_name'])
    else:
        return render_to_response('welcome.html',locals())