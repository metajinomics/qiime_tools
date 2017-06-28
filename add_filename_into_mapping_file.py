#!/usr/bin/python

"""
this script add file name into mapping file
usage: python add_filename_into_mapping_file.py mapping_file > output
example: python add_filename_into_mapping_file.py mapping.txt > mapping_filename_added.txt
"""

import sys

for line in open(sys.argv[1],'r'):
    if line[:1] == "#":
        print line.strip() + '\t' + 'InputFileName'
        continue
    else:
        spl = line.strip().split('\t')
        print line.strip() + '\t' + spl[0] + '.fasta'


