import donkeypart_bluetooth_game_controller as xbox
from inspect import *

def test_device_read_loop(input_device):
    print('reading loop')
    ctlr = BluetoothGameController()
    ctlr.device.read_loop()

def main():
    classes = getmembers(xbox, isclass)
    for name in classes:
        print(name)

main()
