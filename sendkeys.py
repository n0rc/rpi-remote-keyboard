#!/usr/bin/env python3
# (c)2020 n0rc

import keycodes
import os
import re
import sys
import time

from getpass import getpass
from argparse import ArgumentParser

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


def send_key(key, codelist):
    if key in codelist:
        write_report(*codelist[key])
    else:
        print("no keycode found for {}".format(key))


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('-l', '--layout', help='set keyboard layout ("de", "us"), default is "us"' , default='us')
    parser.add_argument('-p', '--password', help='enable password entry mode', action='store_true')
    args, rem = parser.parse_known_args()

    if not re.match(r'^(us|de)$', args.layout) or not args.password and not rem:
        parser.print_help()
        sys.exit(0)

    if os.geteuid() != 0:
        print("please run as root")
        sys.exit(0)

    if args.password:
        string = getpass('password: ')
    else:
        string = rem[0]

    codelist = getattr(keycodes, args.layout.upper())

    # send each character in string
    for key in list(string):
        send_key(key, codelist)
        time.sleep(0.1)

    # send ENTER
    send_enter()
