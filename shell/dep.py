#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob, os,sys

def load_images():
    filesRead = r"%s*.tar" % DIR
    list = glob.glob(filesRead)
    for i in list:
        os.system('docker load < %s -q && rm -rf %s'%(i,i))


def qd():
    if os.path.exists('%shdc_FE'%DIR):
        os.system('rm -rf %shdc_FE/ && mv %shdc_FE %shdc_FE'%(DEPDIR,DIR,DEPDIR))
        print 'hdc_FE deploy finish!'
    else:
        pass

    if os.path.exists('%sdbz_FE'%DIR):
        os.system('rm -rf %sdbz_FE/ && mv %sdbz_FE %sdbz_FE'%(DEPDIR,DIR,DEPDIR))
        print 'dbz_FE deploy finish!'
    else:
        pass
    if os.path.exists('%sopms_FE'%DIR):
        os.system('rm -rf %sopms_FE/ && mv %sopms_FE %sopms_FE'%(DEPDIR,DIR,DEPDIR))
        print 'opms_FE deploy finish!'
    else:
        pass
    if os.path.exists('%sida_FE'%DIR):
        os.system('rm -rf %sida_FE/ && mv %sida_FE %sida_FE'%(DEPDIR,DIR,DEPDIR))
        print 'ida_FE deploy finish!'
    else:
        pass
    if os.path.exists('%ssil_FE'%DIR):
        os.system('rm -rf %ssil_FE/ && mv %ssil_FE %ssil_FE'%(DEPDIR,DIR,DEPDIR))
        print 'sil_FE deploy finish!'
    else:
        pass
    if os.path.exists('%sdsu_FE'%DIR):
        os.system('rm -rf %sdsu_FE/ && mv %sdsu_FE %sdsu_FE'%(DEPDIR,DIR,DEPDIR))
        print 'dsu_FE deploy finish!'
    else:
        pass

    if os.path.exists('%sbi_FE'%DIR):
        os.system('rm -rf %sbi_FE/ && mv %sbi_FE %sbi_FE'%(DEPDIR,DIR,DEPDIR))
        print 'bi_FE deploy finish!'
    else:
        pass



if __name__ == '__main__':
    DIR = '/root/deploy/'
    DEPDIR = '/opt/apps/front/'
    if os.path.exists(DIR):
        pass
    else:
        print 'ERROR:: %s  such File.' %DIR
        exit(1)
    load_images()
    qd()
