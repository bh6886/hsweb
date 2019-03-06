# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import os,sys,glob,re,datetime,time,platform,urllib,urllib2,shutil,logging,json
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import loader, Context, Template
from django import forms

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )



logger = logging.getLogger(__name__)

now_time = datetime.datetime.now()
t =  now_time.strftime('%Y-%m-%d')

def index(req):
    logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
    time = [t]
    return render_to_response('index.html',{'time':time})


#def index(req):
#        return HttpResponse('<h1>hello welcome to Django!</h1>')


def login(request):

    user_loggedin = 'Guest'
    errors_list = []
    if request.method == 'POST':
        #print('pp: ', request.POST.get('username'), request.POST.get('password'))
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        #print('authuser', user)
        if user is not None:
            if user.is_active:
               auth_login(request, user)
               uu = request.user
               loginusername = user
               u = User.objects.get(username=uu)
               return HttpResponseRedirect('/')
            else:
               return HttpResponse('用户没有启用!')
        else:
               return HttpResponse('用户名或者密码错误！')
    else:
        context = {'errors_list': errors_list, 'user_loggedin': user_loggedin}
        return render_to_response('login.html')


def loginout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login/')


@login_required
def index(req):
    return render_to_response('index.html')
