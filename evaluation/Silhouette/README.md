# Silhouette
**Command-line manual**
``` bash
$python  Silhouette.py -f <clustering file> -c <fasta file>
```




# Inputs

The input files of Silhouette.py are: 

Clustering_File which contains the output of the clustering tool. This file should have the folowing format :

``` diff
Cluster_number	seq1 seq2 seq3,...

Example :

1	S483 S483 S483
```

FastaFile which contains nucleotide sequences. This file should have the folowing format :

``` diff
> seq Id
seq

Example :

>S953
CAGGTCCAGCTTGCGCAGTCTGGGGCTGAGGTGAAAAAGCCTGGGGCCTCGGTGAAGGTTTCCTGCAAGGCTTCTGGATACACCTCCAC
```


# Output

## Main output 

The output of Silhouette.py is the value of silhouette:

``` diff
Silhouette : 0.68  
```

## Usage

``` bash
$ python Silhouette.py -f Patient_one.fa  -c Patient_one_Clone_formatted.txt 

   ```

## Silhouette Calculation

The silhouette measures the degree of similarity (cohesion) within a cluster/clone
and the dissimilarity (separation) across different clones. 
This measure was applied to evaluate the performance of
experimental repertoires because it does not require true clone information. 
The silhouette s(i) for a sequence $i$ is defined by

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{100}&space;s(i)&space;=&space;\frac{&space;b(i)&space;-&space;a(i)}{max&space;(a(i),&space;b(i))}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;s(i)&space;=&space;\frac{&space;b(i)&space;-&space;a(i)}{max&space;(a(i),&space;b(i))}" title="s(i) = \frac{ b(i) - a(i)}{max (a(i), b(i))}" /></a>



with a(i) being the average of the distances from the sequence i to any
other sequence in the same cluster/clone, and b(i) being the smallest average
distance of i to all sequence in any other cluster/clone.
We have used the Levenshtein metric to compute the distance between sequences. The Levenshtein distance computes the minimum
number of single-character edition (insertions, deletions or substitutions)
required to transform one sequence into the other. The value of s(i) is
between -1 and 1, a value close to 1 means that i was 
clustered, appropriately. A value close to 0 indicates that i is
on (or very close to) the decision boundary, and it could be placed in another
cluster. Finally, a value close to -1 suggests that i  was placed
in the wrong cluster. We have averaged s(i) over
all sequences to obtain the clustering performance
