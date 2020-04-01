### Polyclonal

Pour le jeu de donnée polyclonal, avec les CDR 3,  sur tous les 1001 faux positifs de l'algorithme louvain, seuls 8 sont mal classés alors qu'ils font la même taille que les faux positifs. Donc pour réduire le recall, il faudrait comparer toutes les séquences, et pas seulement celles de taille différentes. 

Toujour pour polyclonal, il y a un cluster dont 34 séquences sont de taille 17, et 16 séquences sont de taille 56, et 1 de taille 62 (les écarts sont très forts, est-normal ? )

### Monoclonal

Pour monoclonal, c'est encore plus flagrant : on trouve 44 séquences mal classées alors qu'elle font la même taille sur 13365 faux négatifs. 

Il y a beaucoup de faux negatifs car le cluster principal à des membres dans d'autres cluster plus petits, et donc mécaniquement on a beaucoup de faux negatifs (autrement dit on ne rassemble pas assez).

### Oligoclonal

Par contre, pour les données oligoclonale, on trouve des résultats très différents : 2361 sur 2935 séquences ont été mal classées alors qu'elle avaient la même taille que leur cluster principal. Il semble que certaines séquences de la même taille sont très nombreuses, ce qui augmante les chances de mal les classer. Par exemple la taille 32 génère à elle seule 1588 faux positifs pour des séquences de même taille. (54% des faux positifs juste pour cette longueurs).

## Résumé

Monoclonal : 0.33 % des erreurs ne sont pas liées à la longueur des séquences

Oligoclonal : 80 % des erreurs ne sont pas liées à la longueur des séquences

Polyclonal : 0.79 % des erreurs ne sont pas liées à la longueur des séquences. 

### Conclusion

les résultats sont surprenants, et montrent que pour les patient monoclonal et polyclonal, le recall peut être amélioré si on compare toutes les séquences. Pour les patient Oligoclonal, le problème est plus difficile à diagnostiquer. 
