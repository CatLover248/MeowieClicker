from pyautogui import click as clickmouse
from keyboard import is_pressed
from random import randint

version = "V1-BETA1"

def startup():
    print("--------------------------------------")
    print("| MEOWIE CLICKER V1-BETA by FATYCATY |")
    print("--------------------------------------")
    print("Press R to enable AutoClicker and Z to disable AutoClicker!")
    print("MEOWIE CLICKER"+ version +" by FATYCATY")

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
