#!/usr/bin/python
# usage: python get_final_emp_refsoil.py pytable.txt refsoil_filename.txt emp_final_refsoil.txt not_assigned.txt all.txt
# usage: python get_final_emp_refsoil_abun.py most_abun_filename.txt refsoil_filename.txt emp_final_refsoil_abun.txt not_assigned_abun.txt all_abun.txt

import sys

ftable = open(sys.argv[1],'r')
ffilename = open(sys.argv[2],'r')
fwrite = open(sys.argv[3],'w')
fwritenot = open(sys.argv[4],'w')
fwriteall = open(sys.argv[5],'w')
filetable = []
for line in ffilename:
    sep = line.strip().split('\t')
    filetable.append(sep)
#print filetable
for line in ftable:
    idsep = line.strip().split('\t')
    flag = 0
    gi = []
    for i in range(len(filetable)):
        if (filetable[i][2]==idsep[2]):
            fwrite.write(line.strip()+'\t'+filetable[i][0]+'\t'+filetable[i][1]+'\n')
            gi.append(filetable[i][0])
            flag = 1
    if(flag == 0):
        fwritenot.write(line.strip()+'\n')
        fwriteall.write(line.strip()+'\n')
    else:
        fwriteall.write(line.strip()+'\t')
        for i in gi:
            fwriteall.write(i+'\t')
        fwriteall.write('\n')
    
