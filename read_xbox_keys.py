#!/usr/bin/python

from evdev import InputDevice, categorize, ecodes, KeyEvent
device = InputDevice('/dev/input/js0')

def main():
    event = next(device.read_loop())
    print (event)
main()

