Pour executer le code : 

python clustering.py -p data/artficial/Extracted_CDR3/monoclonal_simp_indel_cdr3.fa -s 44 

ou python clustering.py -p et le chemin vers le fichier (à partir de la racine du projet) -s la longueur de séquence pour laquelle on veut représenter le graphe

L'execution de clustering affiche un graphe de clustering obtenu grace à l'algorithme de louvain. 

python clustering.py -p data/artficial/Extracted_CDR3/oligoclonal_simp_indel_cdr3.fa


python  Evaluate_Sim_Cluster.py -p res.txt -t oligoclonal_simp_indel_true_clusters.txt


Cluster results
Total of clusters =  44  Total sequences =  44
44.0 0.0 1475.0 417.0
('Pre = ', 1.0, 'Rec = ', 0.028966425279789335, 'specificity = ', 1.0, 'F-score = ', 0.05630198336532309, 'NumCluster = ', 44, 'NumSeqs = ', 44, ' sumTtC = ', 1519)

