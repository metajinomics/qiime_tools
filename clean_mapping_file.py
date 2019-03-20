#!/usr/bin/python 
"""
This script do ...
usage:
python filename.py arg1...
"""

import sys

def main():
    mapfile = sys.argv[1]
    colnum = 0
    for line in open(sys.argv[1],'r'):
        if line.strip() == "":
            continue
        spl = line.strip().split('\t')
        print('\t'.join(spl))

if __name__ == '__main__':
    main()
