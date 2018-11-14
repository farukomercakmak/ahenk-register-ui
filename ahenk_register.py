#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Ömer Çakmak <farukomercakmak@gmail.com

import os.path
import os
import subprocess
import configparser
import easygui

def register():
    try:
        register_image = "/usr/share/ahenk/icons/ahenk_register.png"
        msg = "Ahenk etki alanında değil, etki alanına almak istiyor musunuz?"
        choices = ["Evet", "Daha Sonra"]
        reply = easygui.buttonbox(msg, image=register_image, title='Ahenk Etki Alanı Kontrolü', choices=choices)
        if reply == "Evet":
            command = "/usr/bin/python3 /usr/share/ahenk/ahenkd.py start"
            process = subprocess.Popen(command, shell=True)
            result_code = process.wait()
            print(result_code)
        else:
            print("Etki alanına alma işlemi iptal edildi")

    except Exception as e:
        print(str(e))

def unregister():
    register_image = "/usr/share/ahenk/icons/ahenk_unregister.png"
    msg = "Ahenk etki alanında, çıkmak istiyor musunuz?"
    choices = ["Evet", "Daha Sonra"]
    reply = easygui.buttonbox(msg, image=register_image, title='Ahenk Etki Alanı Kontrolü', choices=choices)
    if reply == "Evet":
        command = "/usr/bin/python3 /usr/share/ahenk/ahenkd.py unregister"
        process = subprocess.Popen(command, stdin=None, env=None, cwd=None, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        result_code = process.wait()
        p_out = process.stdout.read().decode("unicode_escape")
        p_err = process.stderr.read().decode("unicode_escape")
    else:
        print("Etki alanından çıkma işlemi  iptal edildi")

def ahenk_control():
    PATH = '/etc/ahenk/ahenk.conf'
    rahenk_control_image = "/usr/share/ahenk/icons/ahenk_register.png"
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):

        is_registered()
    else:

        cevap = 'Lütfen ahenk paketinin yüklü olduğundan emin olunuz!'
        choice = easygui.buttonbox(msg=cevap, image=rahenk_control_image, title='Ahenk Etki Alanı Kontrolü',choices=['Tamam'])

def uid():
    config = configparser.ConfigParser()
    config._interpolation = configparser.ExtendedInterpolation()
    config.read("/etc/ahenk/ahenk.conf")
    return config.get('CONNECTION', 'uid')

def is_registered():
    if str(uid()):
        unregister()
    else:
        register()

if __name__ == '__main__':

    ahenk_control()
