# Pour executer le code, depuis ce dossier :

. ./path.sh

# qui demande quel type de données on souhaite utiliser (les choix sont rappelés)

# ensuite, 

python3 $ALGO -p $DATA -r $RESULT 

# calcule les partition optimales, et 

python3 $F1 -p $RESULT -t $REF 

# affiche l'analyse de l'algorithme. Enfin, pour afficher la silhouette : 

python3 $SILHOUETTE -f $DATA -c $RESULT
