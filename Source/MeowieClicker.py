"""
MIT License

Copyright (c) 2022 FatyCaty - Yusuf

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from pyautogui import click as clickmouse
from keyboard import is_pressed
from random import randint
import time

<<<<<<< HEAD
# -R = Offical release
# -B = Beta build
# -D = Developer build

show_debug_information = False
version = "V1-R"

def startup():
    print(" ---------------------------------")
    print("| Meowie Clicker " + version + " by FATYCATY |")
    print(" ---------------------------------")
    print("MeowieClicker "+ version +" by FATYCATY")
    print("Use R to enable Autoclicker and Z to disable Autoclicker.")
    print("Warning: Make sure to not type in incorrect input values!")
    try:
        cps = int(input("CPS[1-8]: "))
        show_debug_information = bool(input("Show Debug Information?[True/False]: "))
        if show_debug_information != True or False:
            print("Something went wrong, make sure to use the right options for inputs.\nQuiting in 5 seconds...")
            time.sleep(5)
            quit
    except:
        print("Something went wrong, make sure to use the right options for inputs.\nQuiting in 5 seconds...")
        time.sleep(5)
        quit("Quiting...")
=======

version = "V1-BETA"

def startup():
    print("--------------------------------------")
    print("| MEOWIE CLICKER V1-BETA by FATYCATY |")
    print("--------------------------------------")
    print("Press R to enable AutoClicker and Z to disable AutoClicker!")
    print("MEOWIE CLICKER "+ version +" by FATYCATY")

    cps = int(input("CPS[1-8]: "))
>>>>>>> b5ab36b8ee4083b0916260e83d9c96d16a4929a2
    return cps 

def clicker(cps):
    click = False
    while True:
        if(is_pressed("r")):
            click = True
            if bool(show_debug_information):
                print(click)
            else:
                continue

        if(is_pressed("z")):
            click = False
            if bool(show_debug_information):
                print(click)
            else:
                continue

        if(click):
            clickmouse(interval=1.00/(cps*3), button="left")
            

def main():
    clicker(startup())



main()
