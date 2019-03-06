# -*- coding: utf-8 -*-
from django import forms
import logging,sys,paramiko,socket
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from blog.views import *

logger = logging.getLogger('django')


class SshHandler:
    def __init__(self,host,port,user):
        self.host=host
        self.port=port
        self.user=user
    def exc(self,quser,shell):
        if quser == 'root':
            return ssh1(self.host,self.port,self.user,'sudo su - %s'%quser,shell)
        else:
            return ssh(self.host,self.port,self.user,'sudo su - %s'%quser,shell)




def ssh(ip,port,user,shell1,shell2):
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,port,user)
        channel = ssh.invoke_shell()
        channel.settimeout(600)
        channel.send('%s\n' % shell1)
        buff = ''
        while not buff.endswith('$ '):
            resp = channel.recv(9999)
            buff +=resp
        buff = ''
        channel.send('%s\n' % shell2)
        while not buff.endswith('$ '):
            resp = channel.recv(9999)
            buff +=resp
        result = buff
        return result
        ssh.close()

def ssh1(ip,port,user,shell1,shell2):
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,port,user)
        channel = ssh.invoke_shell()
        channel.settimeout(600)
        channel.send('%s\n' % shell1)
        buff = ''
        while not buff.endswith('# '):
            resp = channel.recv(9999)
            buff +=resp
        buff = ''
        channel.send('%s\n' % shell2)
        while not buff.endswith('# '):
            resp = channel.recv(9999)
            buff +=resp
        result = buff
        return result
        ssh.close()
