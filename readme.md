# Clustering algotithms

To run the code from this file, use  :

```diff
$. ./settingPath.sh
$python3 $ALGO -p $DATA -r $RESULT 
```

Then, you can see some stats of the algo that you just run :

* F1 score : 

```diff
$python3 $F1 -p $RESULT -t $REF
```

* Silhouette : 

```diff
$python3 $SILHOUETTE -f $DATA -c $RESULT
```

* Time :

```diff
$python3 $TIME -p $DATA
```

* Plot the clusters :

```diff
$python3 $GRAPH -r $RESULT -t $REF
```

* Analysis of the false negatives :

```diff
python3 $ANALYSIS -p $RESULT -t $REF -d $DATA
```

* Merging the resutls of IMGT algorihtm :
```diff
python3 $MERG -c $CLUST_IMGT -d $REF_IMGT -r $RES_IMGT
```


