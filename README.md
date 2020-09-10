Raspberry Pi Remote Keyboard
============================

This is some Bash and Python code to setup and run a **Raspberry Pi Zero W** as a USB HID gadget, e.g. to use it as an USB keyboard with remote access via wifi.

The Pi is back-powered over the USB port of the connected computer and doesn't need an additional power supply.

#### Setup
1. Connect your Pi to your computer using the Pi's Micro-USB **data** port
2. Enable required device tree overlay and modules:
```sh
> echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
> echo "dwc2" | sudo tee -a /etc/modules
```
3. Put `/your/absolute/path/to/gadgetsetup.sh` into `/etc/rc.local` to run the script at boot
4. Reboot the Pi

#### Usage
```sh
> sudo ./sendkeys.py "string"    # send "string" to connected computer, simulating keyboard input
> sudo ./sendkeys.py -l de -p    # send something using german keyboard layout and password mode (no echo)
> sudo ./sendkeys.py -h          # show help
```

#### Credits
* https://github.com/girst/hardpass-sendHID

#### Specs
* https://www.usb.org/sites/default/files/documents/hid1_11.pdf
* https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf
