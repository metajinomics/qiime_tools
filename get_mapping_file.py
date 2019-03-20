
#!/usr/bin/python 
"""
This script do ...
usage:
python filename.py arg1...
"""

import sys

def main():

    samplelist = {}
    for file in sys.argv[1:]:
        if "_L001_" in file:
            spl = file.split("_L001_")
            samplelist[spl0]] = samplelist.get(spl[0],[]).append(spl[1])
        else:
            print ("check file name")

    print(samplelist)


if __name__ == '__main__':
    main()
