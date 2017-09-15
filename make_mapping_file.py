#!/usr/bin/python

"""
this script make mapping file from the files in the directory
usage: python make_mapping_file.py dir_name > mapping.file.txt
example: python make_mapping_file.py merged > mapping.file.txt
"""

import os
import sys
from os import listdir
from os.path import isfile, join
path = sys.argv[1]
files = [f for f in listdir(path) if isfile(join(path,f))]

print "#SampleID\tBarcodeSequence\tLinkerPrimerSequence\tDescription\tInputFileName"
BarcodeSequence = "NNNNNNNNNNNN"
LinkerPrimerSequence = "NNNNNNNNNNNNNNNNNNNNN"
Description = "no_description"
for file in files:
    sample_name = file.replace('.fasta','')
    sample_id = sample_name.replace('_','.')
    result = [sample_id, BarcodeSequence, LinkerPrimerSequence, Description, file]
    print '\t'.join(result)

