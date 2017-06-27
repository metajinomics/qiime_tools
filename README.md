# qiime_tools
This repository have collection of tools to process amplicon data.

### Demultiplex sequences
You need to demultiplex sequences if you get your sequence like this:
```
Undetermined_S0_L001_I1_001.fastq.gz
Undetermined_S0_L001_R1_001.fastq.gz
Undetermined_S0_L001_R2_001.fastq.gz
```
Here, you can use demultiplex_sequences.py to demeltiplex. You will need mapping file (Same file that Qiime reqires)

#### Usage
Note: if your barcode matches in reverse complementary, then use option --reverse_complement 
```
python demultiplex_sequences.py -m mapping_file -b barcode_file -f forward_file -r reverse_file -o output_directory --reverse_complement
```

#### Example
```
python demultiplex_sequences.py -m mapping.txt -b Undetermined_S0_L001_I1_001.fastq.gz -f Undetermined_S0_L001_R1_001.fastq.gz -r Undetermined_S0_L001_R2_001.fastq.gz -o demultiplexed
```

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
