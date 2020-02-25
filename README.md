Raspberry Pi Remote Keyboard
============================

This is some Bash and Python code to setup and run a **Raspberry Pi Zero W** as a USB HID gadget, e.g. to use it as an USB keyboard
with remote access via wifi.

The Pi is back-powered over the USB port of the connected computer and doesn't need an additional power supply.

#### Setup
1. Connect your Pi to your computer using the Pi's Micro-USB **data** port
2. Run `gadgetsetup.sh` at boot time (e.g. via `/etc/rc.local`)

#### Usage
```sh
> sudo ./sendkeys.py "string"
```

#### Example
```sh
> sudo ./sendkeys.py 'Anything is better than nothing!'
```

#### Specifications

* https://www.usb.org/sites/default/files/documents/hid1_11.pdf
* https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf
