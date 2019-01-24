#!/usr/bin/env python
# encoding: utf-8

from pwn import *

def main():

    # return address you want to jump into
    ret_address = 0xXXXXXXX

    # your shellcode
    shellcode = ("\XXXX")

    # manipulate this
    payload = "A"*XXX + p32(ret_address) + shellcode + ???

    # args
    argv = ['/home/ubuntu/proj1/bin/proj1_dep_Anderson',payload, '\x00']

    # Start a process
    p = process(argv = argv)

    # Send the payload to the binary
    # p.send(payload)

    # Pass interaction back to the user
    p.interactive()

if __name__ == "__main__":
    main()
