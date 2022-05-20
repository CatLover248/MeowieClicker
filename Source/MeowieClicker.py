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


#from pyautogui import click as clickmouse
from keyboard import is_pressed
from random import uniform as randdecimalnum
from time import sleep
import win32gui
import win32con
from tkinter import *
import threading

class Clicker:
    def __init__(self,cps, show_debug_information, target_window, randomize_cps,keybind_autoclicker_start, keybind_autoclicker_stop):
        self.cps = cps
        self.show_debug_information = show_debug_information
        self.target_window = target_window
        self.randomize_cps = randomize_cps
        self.keybind_autoclicker_start = keybind_autoclicker_start
        self.keybind_autoclicker_stop = keybind_autoclicker_stop
        self.click = False

# -R = Offical release
# -B = Beta build
# -D = Developer

version = "V6-R"
change_log = "-High CPU usage FIXED.\n-Clicker class and new way to store clicker arguments."

def get_cursor_pos():
    return win32gui.GetCursorPos()

def get_focused_window_title():
    current_focused_window_name = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    return current_focused_window_name

def get_focused_window_hwnd():
    #active_window_name = win32gui.GetWindowText(window)
    #return active_window_name

    hWnd = win32gui.FindWindow(None, str(win32gui.GetWindowText(win32gui.GetForegroundWindow())))
    return hWnd

def startup():

    print(" ---------------------------------")
    print("| Meowie Clicker " + version + " by FATYCATY |")
    print(" ---------------------------------")
    print("   /\\_________________/\\")
    print("  /                     \\")
    print(" /     O             O   \\")
    print("/             w           \\")
    print("MeowieClicker "+ version +" by FatyCaty")
    print("> Change Log for " + version + "\n" + change_log + "")
    print("Warning: Make sure to not type in incorrect input values!!!")

    cps = float(input("CPS[1-100]: "))
    target_window = input("Window for clicker to target(case sensitive)[example: Minecraft 1.8.9]: ")
    show_debug_information = bool(input("Show Debug Information?[True/False]: "))
    randomize_cps = input("Randomize Cps?[True/False]: ")
    keybind_autoclicker_start = input("Autoclicker keybind start[ex: R]: ")
    keybind_autoclicker_stop = input("Autoclicker keybind stop(Cannot be same key as start)[ex: Z]: ")


    return Clicker(cps, show_debug_information, target_window, randomize_cps,keybind_autoclicker_start, keybind_autoclicker_stop)


#def clicker(cps,show_debug_information ,keybind_autoclicker_start,keybind_autoclicker_stop):
def clicker(clicker_obj):  

    while True:
        current_focused_window_title = str(get_focused_window_title())
        if(is_pressed(str(clicker_obj.keybind_autoclicker_start))):
            clicker_obj.click = True
            if bool(clicker_obj.show_debug_information):
                print(clicker_obj.click)
            else:
                continue

        if is_pressed(str(clicker_obj.keybind_autoclicker_stop)):
            clicker_obj.click = False
            if bool(clicker_obj.show_debug_information):
                print(clicker_obj.click)
            else:
                continue

        if clicker_obj.click:
            if  clicker_obj.target_window in current_focused_window_title:
                #clickmouse(interval=1.00/(cps*3), button="left")
                win32gui.PostMessage(get_focused_window_hwnd(), win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, None)
                win32gui.PostMessage(get_focused_window_hwnd(), win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, None)
                if clicker_obj.randomize_cps == "True":
                    sleep((1/clicker_obj.cps) + randdecimalnum(0.001,0.01))
                else:
                    sleep(1/clicker_obj.cps)

def main():
    clicker(startup())

main()