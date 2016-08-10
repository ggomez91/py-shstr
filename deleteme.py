#!/bin/python3

import pyshstr

name=32
pyshstr.Config.debug = True
print (pyshstr.Config)

def a():
    print (pyshstr.shstr("$name"))

a()