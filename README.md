
# Xbox One S Controller
This is a library to connect a [Xbox One S wireless/bluetooth controller](https://www.xbox.com/en-US/xbox-one/accessories/controllers/blue-wireless-controller) to your donkeycar.
 
 >> See the bottom of the page for tested controllers and brands. Beware of knockoffs!



### Install
Install the library.
xpadneo is THE working driver for xbox 1s controller. The one in core currently doesn't work out for me. So follow the instructions on github here:
https://github.com/atar-axis/xpadneo

If you have trouble to connect but able to pair, make sure restart the controller after pairing, then try to connect. 

```bash
pip install https://github.com/chris-han/donkeypart_xbox_one_s_controller.git
```


### Connect your bluetooth controller to the raspberry pi.
1. Start the bluetooth bash tool on your raspberry pi.
```bash
sudo bluetoothctl
power on
scan on
```

2. Turn on your controller in scan mode and look for your controllers name in the bluetoothctl scan results.  This is done by turning over the controller and pushing the sync button until the 4 blue buttons blink
3. Connect to your controller using its id (my controller id is `8C:CD:E8:AB:32:DE`) once you've found it's id. You may have to run these commands several times.
```bash
pair 8C:CD:E8:AB:32:DE
connect 8C:CD:E8:AB:32:DE
trust 8C:CD:E8:AB:32:DE
```
4. Now your controller should show that your controller is connected - the 4 blinking lights turns to one solid light.

5. Run the part script to see if it works. You should see all the button values printed as you press them.
```bash
python ./donkeypart_xbox_1s_controller/donkeypart_xbox_1s_controller/part.py log

The mappings:

            'LS_X': self.update_angle,
            'RT': self.update_throttle, #forward
            'LT': self.update_throttle,
            'B': self.toggle_recording,
            'A': self.toggle_drive_mode,
            'X': self.reset,            
            'RB': self.increment_throttle_scale, 
            'LB': self.decrement_throttle_scale,

6. You can now plug this in as your donkeycar controller in
the manage.py (donkey2.py in the template fodler) script...
```python
from donkeypart_xbox_1s_controller import Xbox1sController 

# then replace your current controller with...
if use_joystick or cfg.USE_JOYSTICK_AS_DEFAULT: 
print("use xbox controller") 
ctr = Xbox1sController(device_search_term="xbox") 
else: 
# This web controller will create a web server that is capable 
# of managing steering, throttle, and modes, and more. 
ctr = LocalWebController(use_chaos=use_chaos) 


```
## modify the __maim__ method with --js
if __name__ == '__main__':
    args = docopt(__doc__)
    cfg = dk.load_config()

    if args['drive']:
        drive(cfg, model_path=args['--model'], use_joystick=args[ '--js'], use_chaos=args['--chaos'])



# Tested Controllers

## Test Drive with Xbox Controller

python ~/mtcar/manage.py drive --js

```
