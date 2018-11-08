#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Ömer Çakmak <farukomercakmak@gmail.com>

import sys
import easygui
import os.path
import os


def register():
    image = "icons/ahenk_unregister.png"
    PATH='./ahenk.conf'
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        print "ahenk.conf var"
        choice = easygui.buttonbox(image=image, title='Ahenk Etki Alanı Kontrolü',choices=['Etki Alanına Al'])
        execfile('register.py')
    else:
        cevap = 'ahenk.conf bulunamadı, ahenk paketinin yüklü olduğundan emin olun!'
        choice = easygui.buttonbox(msg=cevap, image=image, title='Ahenk Etki alanı Kontrolü', choices=['Etki Alanına Al'])


def unregister():
    image = "icons/ahenk_register.png"
    choice = easygui.buttonbox(image=image,title='Ahenk Etki alanı Kontrolü', choices=['Etki Alanından Çıkar'])
    execfile('unregister.py')

if __name__ == '__main__':

    if 'uid =      ' in open('ahenk.conf').read():
        print("Var")
        register()
    else:
        unregister()