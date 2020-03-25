#!/bin/bash

#export 

#read -p 'Quel fichier souhaitez vous utiliser ? ' fichier
#DATA="data/artficial/Extracted_CDR3/$fichier.fa"

read -p 'Entrer l algorithme que vous souhaitez utiliser parmis Louvain ou SpectralClustering: 'algo 
read -p 'Entrez le type de donnée souhaitée parmi mono, oligo ou poly : ' Type
read -p 'Entrez la longueur de séquences souhaitées parmi CDR3 ou Ent : ' long


if ["$algo" = "Louvain"] and ["$long" = "CDR3"]
then
	export ALGO="$PWDW/algoCluster/$algo/LouvainClustering.py"
	export  DATA="$PWD/data/Artificial/Extracted_CDR3/$Type""clonal_simp_indel_cdr3.fa"
	export RESULT="$PWD/algoCluster/$algo/results/$Type""clonal_simp_indel_cdr3.fa"
fi

if ["algo"="Louvain"] and ["$long" = "Ent"]
then
	export ALGO="$PWD/algoCluster/$algo/LouvainClustering.py"
	export DATA="$PWD/data/Artificial/EntireSeq/$Type""clonal_simp_indel_cdr3.fa"
	export RESULT="$PWD/algoCluster/$algo/results/$Type""clonal_simp_indel_cdr3.fa"
fi

if ["algo"="Spectral"] and ["$long"="CDR3"]
then
	export ALGO="$PWD/algoCluster/$algo/SpectralClustering.py"
	export DATA="$PWD/data/Artificial/Extracted_CDR3/$Type""clonal_simp_indel_cdr3.fa"
	export RESULT="$PWD/algoCluster/$algo/results/$Type""clonal_simp_indel_cdr3.fa"
fi

if ["algo"="Spectral"] and ["$long"="Ent"]
then
	export ALGO="$PWD/algoCluster/$algo/SpectralClustering.py"
	export DATA="$PWD/data/Artificial/Extracted_CDR3/$Type""clonal_simp_indel_cdr3.fa"
	export RESULT="$PWD/algoCluster/$algo/results/$Type""clonal_simp_indel_cdr3.fa"
fi

export REF="$PWD/data/Artificial/True_clusters/$Type""clonal_simp_indel_true_clusters.txt"

#Les algos : 
export F1="$PWD/evaluation/F1-score/cluster_based_fscore.py"
export SILHOUETTE="$PWD/evaluation/Silhouette/Silhouette.py"
export TIME="$PWD/evaluation/Exec_time/Exec_time.py"
export RECALL="$PWD/evaluation/Analysis-Recall/analysis-recall.py"
export GRAPH="$PWD/evaluation/Visualisation/show-graph.py"
export ANALYSIS="$PWD/evaluation/Analysis-Recall/essai2.py"
export TESTBENCH="$PWD/algoCluster/Test_Bench/test_bench.py"
#export FASTAFILE="$PWD/data/artficial/True_clusters/$type""clonal_simp_indel_true_clusters.txt"
