# F1-score Evaluation 

## Command-line
``` diff
$python  evaluateSimCluster.py -p <clustering output> -t <true cluster file>
```
where -p takes the formatted clustering output and -t takes the true clustes.

## Input Format
```
1 S22 S135 S136 S635
2 S180 S181 S431 S432 S433 S434 S435 S436 S437 S438 S439 S440
3 S542 S553
 ```
The first column indicates the cluster number, from second column Ids of sequences grouped into that cluster. The sequences Id's are seperated by space.

## Pairwise F1-score calculation

![image of F1-score](cloneCluster/evaluation/F1-score/PR_paiwise.png)