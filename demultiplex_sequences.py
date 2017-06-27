#!/usr/bin/python

"""
# this script separate fastq file into samples
#usage: python demultiplex_sequences.py mapping_file barcode_file fastq R1/R2 directory 
#example python demultiplex_sequences.py -m mapping.txt -b Undetermined_S0_L001_I1_001.fastq.gz -i Undetermined_S0_L001_R1_001.fastq.gz -d R1 -o R1
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
    parser.add_argument('-f', '--forward', dest = "input_file_f", help='input_file_forward')
    parser.add_argument('-r', '--reverse', dest = "input_file_r", help='input_file_reverse')
    parser.add_argument('-d', '--direction', dest = "direction", help='direction')
    parser.add_argument('-o', '--out', dest = "out_dir", help='output_directory')
    parser.add_argument('--reverse', action='store_true', dest = "reverse_comp", default = False, help='reverse compelementary')
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

def read_raw_sequence(filename, ids):
    if (filename[-2:] == 'gz'):
        seqread = gzip.open(filename,'r')
    else:
        seqread = open(filename,'r')
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
    return result

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

            if args.reverse_comp:
                rev = get_rc(spl[1])
                dict[rev] = spl[0]
            else:
                dict[spl[1]] = spl[0] 
    inforead.close()

    #step2: read barcode file
    if (args.barcode_file[-2:] == 'gz'):
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
    
    directions = ['R1','R2']
    #step3: read raw-read file
    result = read_raw_sequence(args.input_file_f, ids)


    #step4: write files
    di = 'R1'
    loc = args.out_dir
    os.mkdir(loc)
    for item in result.items():
        fwrite = open("./"+loc+"/"+item[0]+"."+di+".fastq",'w')
        for x in  item[1]:
            fwrite.write(x+'\n')
        fwrite.close()

if __name__ == '__main__':
    main()
