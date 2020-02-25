#!/usr/bin/env python3
# (c)2020 n0rc

import keycodes
import sys
import time

# key release report = 8 null bytes
report_keyrelease = bytes(8)


def write_report(keycode, modifier=keycodes.NULL):
    report_keypress = bytearray(8)
    report_keypress[0] = modifier
    report_keypress[2] = keycode
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report_keypress)       # send key press
        fd.write(report_keyrelease)     # send key release


def send_enter():
    write_report(keycodes.ENTER)


def send_key(key):
    if key in keycodes.KEYS:
        write_report(*keycodes.KEYS[key])
    else:
        print("no keycode found for {}".format(key))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage:\t{} string".format(sys.argv[0]))
        sys.exit(0)

    string = sys.argv[1]

    # send each character in string
    for key in list(string):
        send_key(key)
        time.sleep(0.1)

    # send ENTER two times
    send_enter()
    time.sleep(0.5)
    send_enter()
