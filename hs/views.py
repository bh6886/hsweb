# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from blog.inits import *
import os
import sys  
from ConfigParser import ConfigParser


CONF = "/opt/skytest/hs/config.conf"
config = ConfigParser()
config.read(CONF)

YY_IP = config.get('IP','yy_ip')
DB_IP = config.get('IP','DB_ip')

xx = '\n##########################################################################################\n'

def time():
     now_time = datetime.datetime.now()
     t =  now_time.strftime('%Y-%m-%d')
     return t
@login_required
def hsps(req):
     obj=SshHandler(YY_IP,22,'root')
     sun = obj.exc('root','docker ps')
     ss = sun.split('\n')
     ss = ss[:-1]
     logger.info('执行模块:%s '%(sys._getframe().f_code.co_name))
     return render_to_response('dep.html',{'ss':ss})

def docker_ps(req, parm):
    obj=SshHandler(YY_IP,22,'root')
    sun = obj.exc('root','docker ps |grep %s --color=no'%parm)
    ss = sun.split('\n')
    ss = ss[:-1]
    return render_to_response('dep.html',{'ss':ss})

def docker_images(req, parm):
    obj=SshHandler(YY_IP,22,'root')
    sun = obj.exc('root','docker images |grep %s --color=no'%parm)
    ss = sun.split('\n')
    ss = ss[:-1]
    return render_to_response('dep.html',{'ss':ss})


@login_required
def hsps_images(req):
     obj=SshHandler(YY_IP,22,'root')
     sun = obj.exc('root','docker images')
     ss = sun.split('\n')
     ss = ss[:-1]
     logger.info('执行模块:%s '%(sys._getframe().f_code.co_name))
     return render_to_response('dep.html',{'ss':ss})


@login_required
def yy_stats(req):
     obj=SshHandler(YY_IP,22,'root')
     aa = obj.exc('root','df -h')
     bb = obj.exc('root','free -m')
     cc = obj.exc('root','cat /proc/cpuinfo| grep "processor"| wc -l')
     sun = 'Disk:'+aa+xx+'\nMemory:\n'+bb+xx+'\nCPU:\n'+cc
     ss = sun.split('\n')
     logger.info('执行模块:%s '%(sys._getframe().f_code.co_name))
     return render_to_response('dep.html',{'ss':ss})

@login_required
def db_stats(req):
     obj=SshHandler(DB_IP,22,'root')
     aa = obj.exc('root','df -h')
     bb = obj.exc('root','free -m')
     cc = obj.exc('root','cat /proc/cpuinfo| grep "processor"| wc -l')
     sun = 'Disk:'+aa+xx+'\nMemory:\n'+bb+xx+'\nCPU:\n'+cc
     ss = sun.split('\n')
     logger.info('执行模块:%s '%(sys._getframe().f_code.co_name))
     return render_to_response('dep.html',{'ss':ss})

@login_required
def docker_restart(req):
    QQ = ('drgs','hdc-manager','etlloader','cas','redis','nginx','opms','message','ida')
    if req.method == 'POST':
       AA = req.POST['a1']
       obj=SshHandler(YY_IP,22,'root')
       sun = obj.exc('root','docker restart %s'%AA)
       ss = sun.split('\n')
       ss = ss[:-1]
       logger.info('执行模块:%s ,重启应用:%s'%(sys._getframe().f_code.co_name,ss))
       return HttpResponse('Restart to %s '%AA)
    else:
        return render_to_response('docker_restart.html',{'QQ':QQ})


def docker_restart_parm(req, parm):
    obj=SshHandler(YY_IP,22,'root')
    sun = obj.exc('root','docker restart %s'%parm)
    ss = sun.split('\n')
    ss = ss[:-1]
    return render_to_response('dep.html',{'ss':ss})

@login_required
def drgs_index(req):
    ss = ''
    if req.method == 'POST':
        AA = req.POST['a1']
        obj = SshHandler(YY_IP, 22, 'root')
        obj.exc('root', 'docker stop drgs && docker rm drgs')
        SHELL = r"docker run -d --restart=always --name drgs \
--net huoshu --ip 172.21.1.5 -p 9998:9998 \
-e ORACLE_ADDR=%s:1521:orcl \
-e LANG='en_US.UTF-8' \
-e HDC_ADDR=%s \
-v /var/log/drgs:/opt/drgs/log \
%s" % (DB_IP,YY_IP,AA)        
        sun = obj.exc('root', SHELL)
        ss = sun.split('\n')
        ss = ss[:-1]
        return render_to_response('dep-log.html',{'ss':ss})
    return render_to_response('drgs_index.html',{'ss':ss})

@login_required
def drgs_log(req):
     obj=SshHandler(YY_IP,22,'root')
     sun = obj.exc('root', 'tail -n 200 /var/log/drgs/drgs.log')
     ss = sun.split('\n')
     ss = ss[:-1]
     logger.info('执行函数名:%s '%(sys._getframe().f_code.co_name))
     return render_to_response('dep-log.html',{'ss':ss})


@login_required
def hdc_index(req):
    ss = ''
    if req.method == 'POST':
        AA = req.POST['a1']
        obj = SshHandler(YY_IP, 22, 'root')
        obj.exc('root', 'docker stop hdc-manager && docker rm hdc-manager')
        SHELL = r"docker run -d --restart=always --name hdc-manager \
--net huoshu --ip=172.21.1.2 -p 8180:8080 \
-v /var/log/hdc-manager:/usr/local/apache-tomcat-8.5.4/logs \
-e ORACLE_ADDR=%s:1521:orcl \
-e LANG='en_US.UTF-8' \
-e HDC_ADDR=%s \
%s" % (DB_IP,YY_IP,AA)
        sun = obj.exc('root', SHELL)
        ss = sun.split('\n')
        ss = ss[:-1]
        return render_to_response('dep-log.html',{'ss':ss})
    return render_to_response('hdc_index.html',{'ss':ss})

@login_required
def hdc_log(req):
     obj=SshHandler(YY_IP,22,'root')
     sun = obj.exc('root', 'tail -n 200 /var/log/hdc-manager/catalina.out')
     ss = sun.split('\n')
     ss = ss[:-1]
     logger.info('执行函数名:%s '%(sys._getframe().f_code.co_name))
     return render_to_response('dep-log.html',{'ss':ss})

@login_required
def etl_index(req):
    ss = ''
    if req.method == 'POST':
        AA = req.POST['a1']
        obj = SshHandler(YY_IP, 22, 'root')
        obj.exc('root', 'docker stop etlloader && docker rm etlloader')
        SHELL = r"docker run -d --restart=always --name etlloader \
--net huoshu --ip 172.21.1.4 -p 8380:8080 \
-e ORACLE_ADDR=%s:1521:orcl \
-e LANG='en_US.UTF-8' \
-e HDC_ADDR=%s \
-v /var/log/etlloader:/opt/etlloader/consolelog \
%s" % (DB_IP,YY_IP,AA)
        sun = obj.exc('root', SHELL)
        ss = sun.split('\n')
        ss = ss[:-1]
        return render_to_response('dep-log.html',{'ss':ss})
    return render_to_response('etl_index.html',{'ss':ss})

@login_required
def etl_log_run(req):
     obj=SshHandler(YY_IP,22,'root')
     sun = obj.exc('root', 'tail -n 200 /var/log/etlloader/console-run.log')
     ss = sun.split('\n')
     ss = ss[:-1]
     logger.info('执行函数名:%s '%(sys._getframe().f_code.co_name))
     return render_to_response('dep-log.html',{'ss':ss})

@login_required
def etl_log_exe(req):
     obj=SshHandler(YY_IP,22,'root')
     sun = obj.exc('root', 'tail -n 200 /var/log/etlloader/console-exe.log')
     ss = sun.split('\n')
     ss = ss[:-1]
     logger.info('执行函数名:%s '%(sys._getframe().f_code.co_name))
     return render_to_response('dep-log.html',{'ss':ss})


@login_required
def opms_index(req):
    ss = ''
    if req.method == 'POST':
        AA = req.POST['a1']
        obj = SshHandler(YY_IP, 22, 'root')
        obj.exc('root', 'docker stop opms && docker rm opms')
        SHELL = r"docker run -d --restart=always \
--net huoshu --ip 172.21.1.8 -p 9977:9977 \
--name opms \
-e ORACLE_ADDR=%s:1521:orcl \
-e HDC_ADDR=%s \
-v /var/log/opms:/opt/opms/log \
%s" % (DB_IP,YY_IP,AA)
        sun = obj.exc('root', SHELL)
        ss = sun.split('\n')
        ss = ss[:-1]
        return render_to_response('dep-log.html',{'ss':ss})
    return render_to_response('opms_index.html',{'ss':ss})

@login_required
def opms_log(req):
     obj=SshHandler(YY_IP,22,'root')
     sun = obj.exc('root', 'tail -n 200 /var/log/opms/logback.log')
     ss = sun.split('\n')
     ss = ss[:-1]
     logger.info('执行函数名:%s '%(sys._getframe().f_code.co_name))
     return render_to_response('dep-log.html',{'ss':ss})


@login_required
def message_index(req):
    ss = ''
    if req.method == 'POST':
        AA = req.POST['a1']
        obj = SshHandler(YY_IP, 22, 'root')
        obj.exc('root', 'docker stop message && docker rm message')
        SHELL = r"docker run -d --restart=always --name message \
--net huoshu --ip 172.21.1.9 \
-e ORACLE_ADDR=%s:1521:orcl \
-e HDC_ADDR=%s \
-v /var/log/message:/opt/message/log \
%s" % (DB_IP,YY_IP,AA)
        sun = obj.exc('root', SHELL)
        ss = sun.split('\n')
        ss = ss[:-1]
        return render_to_response('dep-log.html',{'ss':ss})
    return render_to_response('message_index.html',{'ss':ss})

@login_required
def message_log(req):
     obj=SshHandler(YY_IP,22,'root')
     sun = obj.exc('root', 'tail -n 200 /var/log/message/logback.log')
     ss = sun.split('\n')
     ss = ss[:-1]
     logger.info('执行函数名:%s '%(sys._getframe().f_code.co_name))
     return render_to_response('dep-log.html',{'ss':ss})


@login_required
def dqdep_run(req):
     obj=SshHandler(YY_IP,22,'root')
     sun = obj.exc('root', '/opt/shell/dep.py')
     ss = sun.split('\n')
     ss = ss[:-1]
     logger.info('执行函数名:%s '%(sys._getframe().f_code.co_name))
     return render_to_response('dep-log.html',{'ss':ss})


@login_required
def ida_index(req):
    ss = ''
    if req.method == 'POST':
        AA = req.POST['a1']
        obj = SshHandler(YY_IP, 22, 'root')
        obj.exc('root', 'docker stop ida && docker rm ida')
        SHELL = r"docker run -d --restart=always \
--net huoshu --ip 172.21.1.14 -p 8580:8080 \
--name ida \
-e ORACLE_ADDR=%s:1521:orcl \
-e LANG='en_US.UTF-8' \
-e HDC_ADDR=%s \
-v /var/log/ida:/opt/ida/log \
-v /var/log/ida/testExcel:/opt/ida/testExcel \
%s" % (DB_IP,YY_IP,AA)
        sun = obj.exc('root', SHELL)
        ss = sun.split('\n')
        ss = ss[:-1]
        return render_to_response('dep-log.html',{'ss':ss})
    return render_to_response('ida_index.html',{'ss':ss})

@login_required
def ida_log(req):
     obj=SshHandler(YY_IP,22,'root')
     sun = obj.exc('root', 'tail -n 200  /var/log/ida/ida.log')
     ss = sun.split('\n')
     ss = ss[:-1]
     logger.info('执行函数名:%s '%(sys._getframe().f_code.co_name))
     return render_to_response('dep-log.html',{'ss':ss})


@login_required
def sil_index(req):
    ss = ''
    if req.method == 'POST':
        AA = req.POST['a1']
        obj = SshHandler(YY_IP, 22, 'root')
        obj.exc('root', 'docker stop sil && docker rm sil')
        SHELL = r"docker run -d --restart=always --name sil \
--net huoshu --ip 172.21.1.15 -p 9955:9955 \
-e ORACLE_ADDR=%s:1521:orcl \
-e HDC_ADDR=%s \
-v /var/log/sil:/opt/sil/log \
%s" % (DB_IP,YY_IP,AA)
        sun = obj.exc('root', SHELL)
        ss = sun.split('\n')
        ss = ss[:-1]
        return render_to_response('dep-log.html',{'ss':ss})
    return render_to_response('sil_index.html',{'ss':ss})

@login_required
def sil_log(req):
     obj=SshHandler(YY_IP,22,'root')
     sun = obj.exc('root', 'tail -n 200  /var/log/sil/logback.log')
     ss = sun.split('\n')
     ss = ss[:-1]
     logger.info('执行函数名:%s '%(sys._getframe().f_code.co_name))
     return render_to_response('dep-log.html',{'ss':ss})


@login_required
def dsu_index(req):
    ss = ''
    if req.method == 'POST':
        AA = req.POST['a1']
        obj = SshHandler(YY_IP, 22, 'root')
        obj.exc('root', 'docker stop dsu && docker rm dsu')
        SHELL = r"docker run -d --restart=always --name dsu \
--net huoshu --ip 172.21.1.12 -p 8088:8080 \
-e ORACLE_ADDR=%s:1521:orcl \
-e LANG='en_US.UTF-8' \
-e HDC_ADDR=%s \
-v /var/log/dsu/:/opt/dsu/log \
-v /var/log/dsu/dataset_xml_templet/:/opt/dsu/dataset_xml_templet/ \
%s" % (DB_IP,YY_IP,AA)
        sun = obj.exc('root', SHELL)
        ss = sun.split('\n')
        ss = ss[:-1]
        return render_to_response('dep-log.html',{'ss':ss})
    return render_to_response('dsu_index.html',{'ss':ss})


@login_required
def dsu_log(req):
     obj=SshHandler(YY_IP,22,'root')
     sun = obj.exc('root', 'tail -n 200  /var/log/dsu/dsu.log')
     ss = sun.split('\n')
     ss = ss[:-1]
     logger.info('执行函数名:%s '%(sys._getframe().f_code.co_name))
     return render_to_response('dep-log.html',{'ss':ss})


@login_required
def skydata_index(req):
    ss = ''
    if req.method == 'POST':
        AA = req.POST['a1']
        obj = SshHandler(YY_IP, 22, 'root')
        obj.exc('root', 'docker stop skydata-se && docker rm skydata-se')
        SHELL = r"docker run -d --restart=always --name skydata-se \
--net huoshu --ip=172.21.1.3 -p 8280:8080 \
-v /var/log/skydata-se:/usr/local/apache-tomcat-8.5.4/logs \
-e ORACLE_ADDR=%s \
-e LANG='en_US.UTF-8' \
-e HDC_ADDR=%s \
%s" % (DB_IP,YY_IP,AA)
        sun = obj.exc('root', SHELL)
        ss = sun.split('\n')
        ss = ss[:-1]
        return render_to_response('dep-log.html',{'ss':ss})
    return render_to_response('skydata_index.html',{'ss':ss})


@login_required
def skydata_log(req):
     obj=SshHandler(YY_IP,22,'root')
     sun = obj.exc('root', 'tail -n 200   /var/log/skydata-se/catalina.out')
     ss = sun.split('\n')
     ss = ss[:-1]
     logger.info('执行函数名:%s '%(sys._getframe().f_code.co_name))
     return render_to_response('dep-log.html',{'ss':ss})
