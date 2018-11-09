#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Ömer Çakmak <farukomercakmak@gmail.com>

import easygui
import os.path
import os
import subprocess
from base.system.system import System
import configparser


def register():
    register_image = "/usr/share/ahenk/icons/ahenk_register.png"
    msg = "Ahenk etki alanında değil, etki alanına almak istiyor musunuz?"
    choices = ["Evet", "Daha Sonra"]
    reply = easygui.buttonbox(msg, image=register_image, choices=choices)
    if reply == "Evet":
        command = "sudo python3 /usr/share/ahenk/ahenkd.py start"
        process = subprocess.Popen(command, stdin=None, env=None, cwd=None, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        result_code = process.wait()
        p_out = process.stdout.read().decode("unicode_escape")
        p_err = process.stderr.read().decode("unicode_escape")
    else:
       print("No")


def ahenk_control():
    PATH = '/etc/ahenk/ahenk.conf'
    rahenk_control_image = "/usr/share/ahenk/icons/ahenk_register.png"
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):

        register()
    else:
        print "ahenk.conf yok"
        cevap = 'ahenk.conf bulunamadı, ahenk paketinin yüklü olduğundan emin olun!'
        choice = easygui.buttonbox(msg=cevap, image=rahenk_control_image, title='Ahenk Etki alanı Kontrolü',
                                   choices=['Tamam'])

def is_registered(self):
    try:
        if str(System.Ahenk.uid()):
            return True
            print("register oldu")
        else:
            return False
            print("register değil")
    except:
        return False


def unregister():
    register_image = "/usr/share/ahenk/icons/ahenk_register.png"
    msg = "Ahenk etki alanında, çıkmak istiyor musunuz?"
    choices = ["Evet", "Daha Sonra"]
    reply = easygui.buttonbox(msg, image=register_image, choices=choices)
    if reply == "Evet":
        print("Evet")
    else:
        print("No")

if __name__ == '__main__':

    ahenk_control()