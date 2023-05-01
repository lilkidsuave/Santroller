#!/usr/bin/env python3
from os.path import join
from pprint import pp
import subprocess
import sys
import re
import traceback

try:
    import usb
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyusb"])
try:
    import libusb_package
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "libusb-package"])

import libusb_package

import usb.core
import usb.util
import os

REBOOT = 48
BOOTLOADER = 49
BOOTLOADER_SERIAL = 50

Import("env")


class Context:
    def __init__(self):
        self.meta = ""


def post_upload(source, target, env):
    if "/arduino_uno/" in str(source[0]) or "/arduino_mega/" in str(source[0]) or "/arduino_mega_2560/" in str(source[0]) or "/arduino_mega_adk/" in str(source[0]):
        env.TouchSerialPort("$UPLOAD_PORT", 2400)
    if "arduino_uno_usb" in str(source[0]) or "arduino_mega_2560_usb" in str(source[0]) or "arduino_mega_adk_usb" in str(source[0]):
        print("searching for uno")
        new_env = None
        while not new_env:
            dev = libusb_package.find(idVendor=0x03eb, idProduct=0x0001)
            if dev:
                new_env = "arduino_uno"
                break
            dev = libusb_package.find(idVendor=0x03eb, idProduct=0x0010)
            if dev:
                new_env = "arduino_mega_2560"
                break
            dev = libusb_package.find(idVendor=0x03eb, idProduct=0x003f)
            if dev:
                new_env = "arduino_mega_adk"
                break
            dev = libusb_package.find(idVendor=0x1209, idProduct=0x2882)
            if not dev:
                dev = libusb_package.find(idVendor=0x1209, idProduct=0x2884)
            if dev:
                try:
                    dev.detach_kernel_driver(0)
                except:
                    pass
                try:
                    dev.ctrl_transfer(0x21, BOOTLOADER_SERIAL)
                    dev.ctrl_transfer(0x21, 0x09, BOOTLOADER_SERIAL)
                except Exception as e:
                    print(e)
                    pass
        cwd = os.getcwd()
        os.chdir(env["PROJECT_DIR"])
        print(f"Calling {new_env}")
        subprocess.run([sys.executable,"-m","platformio", "run", "--target", "upload", "--environment", new_env], stderr=subprocess.STDOUT)
        os.chdir(cwd)
        env.AutodetectUploadPort()
        env.TouchSerialPort("$UPLOAD_PORT", 2400)


env.AddPostAction("upload", post_upload)
