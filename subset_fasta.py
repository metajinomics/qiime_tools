#!/usr/bin/python

#usage: subset_fasta.py list_id repset.fna > sub.fna

import sys

d = {}
for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    d[spl[0]] = spl[0]

flag = 0
for line in open(sys.argv[2],'r'):
    if line[:1] == ">":
        flag = 0
        spl = line[1:].strip().split(' ')
        if d.has_key(spl[0]):
            flag = 1
            print line,
    else:
        if flag == 1:
            print line,
