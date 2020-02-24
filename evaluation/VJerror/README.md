# VJ annotation errors
**Command-line manual**

For evaluating the consistency of genes V and J across all infered
clusters.




# Input 

The main input files of VJerror.py are: 

1- VJ_file which contains the the IGHV and IGHJ identity of each sequence. This file should have the folowing format :

``` diff
Seq ID IGHV IGHJ

Example :

S1	IGHV3-21*01	IGHJ6*02
```
For the sequence coming from patients, you can use the Format_output_realdata.py to format the output of VDJ-assignment's step of IMGT/high-vquest to the acceptable input file of VJerror.py.
``` bash
$ python Format_output_realdata.py -i 1_Summary.txt
```

2- Predicted_clusters_File which contains the output of clustring tool. This file should have the folowing format :

``` diff
Cluster_number	seq1 seq2 seq3,...

Example :

1	S483-12 S483-9 S483-3 
```




# Output

## Main output files

The  output of VJerror.py are the VJ error value:

``` diff
VJerror : 0.002
```

## Usage

``` bash
$ python VJerror.py -v Patient_one_VJ.txt -c Patient_one_Mixclus_output.txt
```