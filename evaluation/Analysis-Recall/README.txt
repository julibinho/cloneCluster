# Script d'analyse du recall pour les séquences monoclonales, particulièrement avec l'algorithme louvain pour tenter de comprendre pourquoi les résultats sont mauvais.

Recall = True Positives
True Positives + False negatives


donc si le recall est petit c'est qu'il y a beaucoup de false negative


J'ai refais le calcul du recall pour les données monoclonal, et je trouve comme valeurs : 
false negative :  74990
true positive : 170407
recall = 170407 / (170407 + 74990) = 0.69

l'algorithme dans F1-score trouve : 
false negative :  13365
true positive :  902
recall = 902 / (902 + 13365) = 0.063  


Le plus gros cluster dans true cluster compte 700 séquences, et dans nos résultats, sur ces 700 séquences, 582 appartiennent au même cluster (le 0 dans resultat), et 118 à d'autres clusters.

donc pour les false negative, il y a au moins 582*118 = 68676 paires de séquences, sans compter les différences parmis les 118, et seulement pour un cluster. C'est supérieur aux 13365 false negative trouvés dans l'algo F1. Je n'ai pas très bien compris comment fonctionne l'algorithme F1, mais est-ce qu'il est possible que l'algo ne prennent pas en compte tous les false positive et tous les false négative ? 

Mes codes sont dans le fichier analysis-recall, et les listes qui sont affichées sont le cluster assignés par l'algo pour toutes les séquences d'un même cluster dans true cluster (donc si toutes les valeurs sont les mêmes, il n'y a aucun false negative, et que des true positive).
Si j'ai fait une erreur dans le calcul du recall, est-ce que ce serait possible de me dire ce qui ne va pas ? 

j'espère que ma question est claire...
