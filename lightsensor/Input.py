#!/usr/bin/env python
#_*_ coding: utf-8 _*_

import serial
import time
import json

def main():
    name = 1
    dict = {}
    s = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(2)
    print s.portstr
    for num in range(200):
        dict[name] = int(s.readline())
        name += 1
    f = open('data.json', 'w')
    json.dump(dict, f)
    f.close()

if __name__ == '__main__':
    main()

