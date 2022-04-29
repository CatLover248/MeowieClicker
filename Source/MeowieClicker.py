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


from ctypes.wintypes import LPARAM
from pyautogui import click as clickmouse
from keyboard import is_pressed
from random import uniform as randdecimalnum
from time import sleep
import win32gui
import win32con


# -R = Offical release
# -B = Beta build
# -D = Developer 
show_debug_information = False
version = "V4-R"
change_log = "-New clicking method(bypasses Lunar)\n-Custom target windows\n-Code improvments\n-Support for Cps higher than 8\n-Cute cat art fixed\nCps Randomization"

def get_cursor_pos():
    return win32gui.GetCursorPos()

def get_focused_window(window_title):

    #window = win32gui.GetForegroundWindow()
    #active_window_name = win32gui.GetWindowText(window)
    #return active_window_name

    hWnd = win32gui.FindWindow(None, str(window_title))
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
    print("Use R to enable Autoclicker and Z to disable Autoclicker.")
    print("Warning: Make sure to not type in incorrect input values!")
    
    cps = float(input("CPS[1-100]: "))
    target_window = input("Window for clicker to target(case sensitive)[example: Minecraft 1.8.9]: ")
    show_debug_information = input("Show Debug Information?[True/False]: ")
    randomize_cps = input("Randomize Cps?[True/False]: ")
    keybind_autoclicker_start = input("Autoclicker keybind start[ex: R]: ")
    keybind_autoclicker_stop = input("Autoclicker keybind stop(Cannot be same key as start)[ex: Z]: ")
    #if ((show_debug_information.lower().strip() != "true" or "false") or keybind_autoclicker_start.len() and keybind_autoclicker_stop.len() == 1):
        #print("Something went wrong, make sure to use the right options for inputs and only choose one character for your Autoclicker keybind.\nQuiting in 5 seconds...")
        #sleep(5)
        #quit()
    
    
    return [cps, show_debug_information, target_window, randomize_cps,keybind_autoclicker_start, keybind_autoclicker_stop]

#def clicker(cps,show_debug_information ,keybind_autoclicker_start,keybind_autoclicker_stop):
def clicker(args_to_clicker):
    
    cps = args_to_clicker[0]
    show_debug_information = args_to_clicker[1]
    target_window = str(args_to_clicker[2])
    randomize_cps = args_to_clicker[3]
    keybind_autoclicker_start = args_to_clicker[4]
    keybind_autoclicker_stop = args_to_clicker[5]

    click = False
    while True:
        if(is_pressed(str(keybind_autoclicker_start))):
            click = True
            if bool(show_debug_information):
                print(click)
            else:
                continue

        if is_pressed(str(keybind_autoclicker_stop)):
            click = False
            if bool(show_debug_information):
                print(click)
            else:
                continue
        #Lunar window: Lunar Client (1.8.9-c888646/master)
        if click:
            #clickmouse(interval=1.00/(cps*3), button="left")
            win32gui.PostMessage(get_focused_window(target_window), win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, None)
            win32gui.PostMessage(get_focused_window(target_window), win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, None)
            if randomize_cps == "True":
                sleep((1/cps) + randdecimalnum(0.001,0.01))
            else:
                sleep(1/cps)
            
            
        


def main():
    clicker(startup())

    



main()