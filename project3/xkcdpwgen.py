#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 15:45:33 2023

@author: matthewcerillo
"""

from random import randint
import sys, getopt

word = 4
capital = 0
number = 0
symbol = 0
special = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "<", ">", "?", "~"]

try:
    opts, args = getopt.getopt(sys.argv[1:], "hc:w:n:s:", ["help", "capitals=", "word=", "number=", "symbol="])
except getopt.GetoptError:
    print("usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]")
    sys.exit(2)
    
for opt, arg in opts:
    if opt in ('-h', "--help"):
        print("usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]\n\n" +
              "Generate a secure, memorable password using the XKCD method\n\n" +
              "optional arguments:\n" +
              "    -h, --help            show this help message and exit\n" +
              "    -w WORDS, --words WORDS\n" +
              "                          include WORDS words in the password (default=4)\n" +
              "    -c CAPS, --caps CAPS  capitalize the first letter of CAPS random words\n" +
              "                          (default=0)\n" +
              "    -n NUMBERS, --numbers NUMBERS\n" +
              "                          insert NUMBERS random numbers in the password\n" +
              "                          (default=0)\n" +
              "    -s SYMBOLS, --symbols SYMBOLS\n" +
              "                          insert SYMBOLS random symbols in the password\n" +
              "                          (default=0)")
        sys.exit()
    elif opt in ("-w", "--word"):
        words = int(arg)
    elif opt in ["-c", "--cap"]:
        caps = int(arg)
    elif opt in ["-n", "--number"]:
        numbers = int(arg)
    elif opt in ["-s", "--symbol"]:
        symbols = int(arg)

with open('words2.txt') as f:
    lines = f.read().splitlines()

password = ''
for i1 in range(word):
    x = randint(0, len(lines) - 1)
    temp = lines[x]
    if capital >= (word - i1):
        temp = temp[0].upper() + temp[1:]
    elif capital > 0:
        if randint(0, word) < capital:
            temp = temp[0].upper() + temp[1:]
            capital -= 1
    password += temp

for i2 in range(number):
    x = randint(0, len(password) - 1)
    password = password[0:x] + str(randint(0, 9)) + password[x:]

for i3 in range(symbol):
    x = randint(0, len(password) - 1)
    password = password[0:x] + special[randint(0, len(special) - 1)] + password[x:]

print(password)








