#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Ömer Çakmak <farukomercakmak@gmail.com>

import sys
import easygui
import os.path
import os
#from base.system.system import System
import subprocess



def register():
    register_image = "/usr/share/ahenk/icons/ahenk_unregister.png"
    PATH='/etc/ahenk/ahenk.conf'
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        print "ahenk.conf var"

        msg = "Etki Alanına Almak İstiyor musunuz?"
        title = "Ahenk Etki Alanı Kontrolü"
        image = register_image
        #choice = easygui.buttonbox
        if easygui.buttonbox(msg, title):  # show a Continue/Cancel dialog
            pass  # user chose Continue
        else:  # user chose Cancel
            sys.exit(0)

        command = "sudo python3 /usr/share/ahenk/ahenkd.py start"
        process = subprocess.Popen(command, stdin=None, env=None, cwd=None, stderr=subprocess.PIPE,
                                   stdout=subprocess.PIPE, shell=True)
        result_code = process.wait()
        p_out = process.stdout.read().decode("unicode_escape")
        p_err = process.stderr.read().decode("unicode_escape")

    else:
        cevap = 'ahenk.conf bulunamadı, ahenk paketinin yüklü olduğundan emin olun!'
        choice = easygui.buttonbox(msg=cevap, image=image, title='Ahenk Etki alanı Kontrolü', choices=['Etki Alanına Al'])


def unregister():
    register_image = "/usr/share/ahenk/icons/ahenk_register.png"


    msg = "Ahenk etki alanında, çıkmak istiyor musunuz?"
    choices = ["Evet", "Daha Sonra"]
    reply = easygui.buttonbox(msg, image=register_image, choices=choices)
    if reply == "Yes":
        print("Evet")
    else:
        print("No")


   if __name__ == '__main__':

       unregister()
       #register()