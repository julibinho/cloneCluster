# Clustering and merging algotithms

## To run the code from this file, use  :
### For a clustering algorithm : 
```diff
$. ./settingPath.sh
$python3 $ALGO -p $DATA -r $RESULT 
```
Warning : If using Gclust algo : run with Python2 and not Python3
### For a merging algorithm :

```diff
$. ./settingPath.sh
$python3 $ALGO -c $CLUST -d $DATA -r $RESULT
```
 
## Then, you can see some stats of the algo that you just run :
* Silhouette : 

```diff
$python3 $SILHOUETTE -f $DATA -c $RESULT
```

* Time :

```diff
$python3 $TIME -p $DATA
```

## And only for simulated data : 

* F1 score : 

```diff
$python3 $F1 -p $RESULT -t $REF
```

* Plot the clusters :

```diff
$python3 $GRAPH -r $RESULT -t $REF
```

* Analysis of the false negatives :

```diff
$python3 $ANALYSIS -p $RESULT -t $REF -d $DATA
```

## For Gclust only on Artificial CDR3 sequences of IMGT :

```diff
$python2 $ALGO -p $DATA_IMGT -r $RESULT
```
```diff
$python3 $F1 -p $RESULT -t $REF_IMGT
```
