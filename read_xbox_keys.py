#!/usr/bin/python
from evdev import *
gamepad = InputDevice('/dev/input/event0')

def main():
    for event in gamepad.read_loop():
        print (event)


main()

