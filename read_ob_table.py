#!/usr/bin/python
#python read_ob_table.py abundance.txt pytable_abun.txt
import sys

def add_null(table,lo):
    if(len(table)<lo):
        table.append('null')

def add_lin(pysep,lo,letter,temp):
    if(len(pysep)>lo):
        if(pysep[lo][-2:]==letter):
            temp.append(pysep[lo][:-2])
        else:
            exc = pysep[lo].split('.')
            temp.append(exc[0])
    add_null(temp,lo+1)

def main():
    table = []
    fread = open(sys.argv[1],'r')
    let = ['_k','_p','_c','_o','_f','_g','_s']
    for line in fread:
        inisep = line.strip().split('\t')
        obser = inisep[1].split(': ')
        pysep = inisep[0].split('__')
        temp = []

        #add filename
        temp.append(inisep[0])

        #add lineage
        for i in range(1,7):
            add_lin(pysep,i,let[i],temp)
        #add abundance
        temp.append(obser[1])
        table.append(temp)

    #print table
    fwrite = open(sys.argv[2],'w')
    for line in table:
        for i in line:
            fwrite.write(i+'\t')
        fwrite.write('\n')

if __name__ == '__main__':
    main()
