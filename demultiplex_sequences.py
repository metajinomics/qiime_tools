#!/usr/bin/python

"""
# this script separate fastq file into samples
#usage: python demultiplex_sequences.py mapping_file barcode_file fastq R1/R2 directory 

"""


import sys
from string import maketrans
import os
import gzip
import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='this script separate fastq file into samples')

    parser.add_argument('-m', '--map', dest = "mapping_file", help='mapping file')
    parser.add_argument('-b', '--barcode', dest = "barcode_file", help='barcode file')
    parser.add_argument('-i', '--in', dest = "input_file", help='input_file')
    parser.add_argument('-d', '--direction', dest = "direction", help='direction')
    parser.add_argument('-o', '--out', dest = "out_dir", help='output_directory')
    return parser

def add_seq(seq,ids,result):
    if( ids.has_key(seq[0].split(' ')[0])):
        samid = ids[seq[0].split(' ')[0]]
        if (result.has_key(samid)):
            temp = result[samid]
            temp.append('\n'.join(seq))
            result[samid]=temp
        else:
            result[samid]= ['\n'.join(seq)]

def get_rc(seq):
    seq = seq.upper()
    trans = maketrans("AGCT","TCGA")
    seq = seq.translate(trans,'xm')
    seq = seq[::-1]
    return seq

def check_barcode(seq,dict,result):
    barcode = seq[1]
    if( dict.has_key(barcode)):
        samid = dict[barcode]
        if (result.has_key(samid)):
            print "duplicated id"
        else:
            result[seq[0].split(' ')[0]]=dict[barcode]

def main():
    parser = get_parser()

    args = parser.parse_args()
    

    #step1: read mapping file
    dict = {}
    inforead = open(args.mapping_file,'r')
    for line in inforead:
        if (line[:1] == "#"):
            continue
        else:
            spl = line.strip().split('\t')
            dict[spl[1]] = spl[0]
            #rev = get_rc(spl[1])
            #dict[rev] = spl[0]
    inforead.close()

    #step2: read barcode file
    if (sys.argv[2][-2:] == 'gz'):
        barread = gzip.open(args.barcode_file,'r')
    else:
        barread = open(args.barcode_file,'r')
    seq  = [] 
    ids = {}
    for n,line in enumerate(barread):
        if( n % 4 == 3):
            seq.append(line.strip())
            check_barcode(seq,dict,ids)
            seq = []
        else:
            seq.append(line.strip())
    barread.close()
    
    #step3: read raw-read file
    if (sys.argv[3][-2:] == 'gz'):
        seqread = gzip.open(args.input_file,'r')
    else:
        seqread = open(args.input_file,'r')
    seq = []
    result = {}
    for n,line in enumerate(seqread):
        if (n % 4 == 3):
            seq.append(line.strip())
            add_seq(seq,ids,result)
            seq = []
        else:
            seq.append(line.strip())
    seqread.close()

    #step4: write files
    di = args.direction
    loc = args.out_dir
    os.mkdir(loc)
    for item in result.items():
        fwrite = open("./"+loc+"/"+item[0]+"."+di+".fastq",'w')
        for x in  item[1]:
            fwrite.write(x+'\n')
        fwrite.close()

if __name__ == '__main__':
    main()
