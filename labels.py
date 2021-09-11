#!/usr/bin/env python
# -*- coding: utf-8 -*-

import escpos.printer
import sys

texts = sys.argv[1:]

print("Connecting to printer")
p = escpos.printer.File("/dev/usb/lp0")


print("Printing")
for text in texts:
    print(f"> {text}")
    p.set(double_height=True, double_width=True)
    p.textln(text)
    p.textln("")
