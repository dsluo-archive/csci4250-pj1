#!/usr/bin/env python
# encoding: utf-8

import struct
import sys, getopt

def main(argv):

    with open(sys.argv[1], 'rb') as f:
        while 1:
            byte_s = f.read(1)
            if not byte_s:
                break
            #data = struct.unpack("<b",byte_s)[0]
            #sys.stdout.write('\\x' + format(data, '02x'))
            # sys.stdout.write('\\x' + hex(ord(byte_s)))
            sys.stdout.write('\\x' + format(ord(byte_s),"02x"))

if __name__ == "__main__":
       main(sys.argv)
