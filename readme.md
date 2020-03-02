# Clustering algotithms

To run the code from this file, use  :

```diff
$. ./path.sh
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


