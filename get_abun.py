#!/usr/bin/python                                                                   
# usage: python get_abun.py RefSoilToEMPsoil.out.txt refsoil_abun.txt 
import re
import sys
import glob

def search(search_term):
    for filename in glob.glob('*.summary'):
        for line in open(filename,'r'):
            if re.search(search_term,line):
                return line.strip()

def main():
    fread = open(sys.argv[1],'r')
    fwrite = open(sys.argv[2],'w')
    for line in fread:
        seid = line.strip().split('\t')
        search_term = (" "+seid[1]+': ')
        abun = search(search_term)
        fwrite.write(seid[0]+'\t'+seid[1]+'\t'+abun.split(':')[1]+'\n')


if __name__ == '__main__':
    main()
