
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
            temp = samplelist.get(spl[0],[])
            temp.append(spl[1])
            samplelist[spl[0]] = temp
        else:
            print ("check file name")


    print ("#SampleID\tBarcodeSequence\tLinkerPrimerSequence\tInputFileName\tDescription")
    BarcodeSequence = "NNNNNNNNNNNN"
    LinkerPrimerSequence = "NNNNNNNNNNNNNNNNNNNNN"
    Description = "no_description"

    for item in samplelist.items():
        inputfilename = item[0]+".fasta"
        re1 = item[0].replace('_','.')
        sampleid = re1.replace('-','.')
        reult = [sampleid, BarcodeSequence, LinkerPrimerSequence, inputfilename, Description]
        print('\t'.join(result)

if __name__ == '__main__':
    main()
