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
from time import sleep
import win32gui

# -R = Offical release
# -B = Beta build
# -D = Developer 
show_debug_information = False
version = "V2-R"
change_log = "- Added so that clicker only clicks in Minecraft(Lunar client, LabyMod, Badlion)\n- Partnerd up with EmpathyClient by LukeBTW\n- Added Custom Keybinds to AutoClicker\n- More code stuff..."

def get_focused_window():

    window = win32gui.GetForegroundWindow()
    active_window_name = win32gui.GetWindowText(window)
    return active_window_name

def startup():
    
    print(" ---------------------------------")
    print("| Meowie Clicker " + version + " by FATYCATY |")
    print(" ---------------------------------")
    print("MeowieClicker "+ version +" by FatyCaty")
    print("> Change Log for " + version + "\n" + change_log + "")
    print("Use R to enable Autoclicker and Z to disable Autoclicker.")
    print("Warning: Make sure to not type in incorrect input values!")
    
    cps = int(input("CPS[1-8]: "))
    show_debug_information = input("Show Debug Information?[True/False]: ")
    keybind_autoclicker_start = input("Autoclicker keybind start[ex: R]: ")
    keybind_autoclicker_stop = input("Autoclicker keybind stop(Cannot be same key as start)[ex: Z]: ")
    #if ((show_debug_information.lower().strip() != "true" or "false") or keybind_autoclicker_start.len() and keybind_autoclicker_stop.len() == 1):
        #print("Something went wrong, make sure to use the right options for inputs and only choose one character for your Autoclicker keybind.\nQuiting in 5 seconds...")
        #sleep(5)
        #quit()
    
    
    return [cps, show_debug_information, keybind_autoclicker_start, keybind_autoclicker_stop]

#def clicker(cps,show_debug_information ,keybind_autoclicker_start,keybind_autoclicker_stop):
def clicker(args_to_clicker):

    cps = args_to_clicker[0]
    show_debug_information = args_to_clicker[1]
    keybind_autoclicker_start = args_to_clicker[2]
    keybind_autoclicker_stop = args_to_clicker[3]

    click = False
    while True:
        
        current_focused_window = get_focused_window()

        if(is_pressed(str(keybind_autoclicker_start))):
            click = True
            if bool(show_debug_information):
                print(click)
            else:
                continue

        if(is_pressed(str(keybind_autoclicker_stop))):
            click = False
            if bool(show_debug_information):
                print(click)
            else:
                continue
        
        if(click and (("Minecraft" in current_focused_window) or ("Lunar" in current_focused_window) or ("Badlion" in current_focused_window))):
            clickmouse(interval=1.00/(cps*3), button="left")
            
        


def main():
    clicker(startup())



main()