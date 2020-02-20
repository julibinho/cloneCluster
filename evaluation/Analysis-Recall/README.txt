# Script d'analyse du recall pour les séquences monoclonales, particulièrement avec l'algorithme louvain pour tenter de comprendre pourquoi les résultats sont mauvais.

Recall = True Positives
True Positives + False negatives


donc si le recall est petit c'est qu'il y a beaucoup de false negative
faux positifs : les paires qui sont clasées dans le même cluster, mais qui ne le sont pas dans true_cluster

