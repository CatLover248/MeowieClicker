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


version = "V1-BETA"

def startup():
    print("--------------------------------------")
    print("| MEOWIE CLICKER V1-BETA by FATYCATY |")
    print("--------------------------------------")
    print("Press R to enable AutoClicker and Z to disable AutoClicker!")
    print("MEOWIE CLICKER "+ version +" by FATYCATY")

    cps = int(input("CPS[1-8]: "))
    return cps 

def clicker(cps):
    click = False
    while True:
        if(is_pressed("r")):
            click = True
            print(click)

        if(is_pressed("z")):
            click = False
            print(click)
        if(click):
            clickmouse(interval=1.00/(cps*3), button="left")
            

def main():
    clicker(startup())



main()
