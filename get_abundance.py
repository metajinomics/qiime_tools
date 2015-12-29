#!/usr/bin/python

#this script get observation after run split_libraries.py
#usage: python get_observation.py
#then, the program read all .summary files in the folder and make observation.txt



#import os
#for filename in os.listdir(os.getcwd()):
#    print filename
import glob
fwrite = open('abundance.txt','w')
for filename in glob.glob('*.summary'):
    print filename
    fo = open(filename,'r')
    line = fo.readline()
    line = fo.readline()
    line = fo.readline().strip()
    print line
    fwrite.write(filename+'\t'+line+'\n')
    fo.close()
