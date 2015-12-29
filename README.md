# qiime_tools
qiime_tools

### get_observation.py
this script get observation after run split_libraries.py

usage: python get_observation.py

then, the program read all .summary files in the folder and make observation.txt

## How to get biggiest gap by abundance
### step 1
```
python get_filenaem.py RefSoilToEMPsoil.out.txt refsoil_filename.txt
```
### step 2
get abundance from summary file
```
python get_abundance.py
```
then you will see abundance.txt
### step 3
```
python read_ob_table.py abundance.txt pytable_abun.txt
```
### step 4
```
python get_final_emp_refsoil.py pytable_abun.txt refsoil_filename.txt emp_final_refsoil_abun.txt not_assigned_abun.txt all_abun.txt
```
### step 5
in excel open not_assigned_abun.txt 
