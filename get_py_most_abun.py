#!/usr/bin/python
# python get_py_most_abun.py 200mostAbunOTU_w_counts.txt most_abun_filename.txt
import sys
import re
import glob

def search(search_term):
    for filename in glob.glob('*.summary'):
        for line in open(filename,'r'):
            if re.search(search_term,line):
#                return line.strip()
                return filename

def main():
    fread = open(sys.argv[1],'r')
    fwrite = open(sys.argv[2],'w')
    for line in fread:
        seid = line.strip().split('\t')
        search_term = (" "+seid[0]+': ')
        abun = search(search_term)
        fwrite.write(seid[0]+'\t'+seid[1]+'\t'+abun+'\n')

if __name__ == '__main__':
    main()
