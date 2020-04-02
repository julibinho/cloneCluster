#!/bin/bash

#export 

#read -p 'Quel fichier souhaitez vous utiliser ? ' fichier
#DATA="data/artficial/Extracted_CDR3/$fichier.fa"

read -p 'Entrez l algorithme que vous souhaitez utiliser parmis Louvain ou SpectralClustering : ' algo 
read -p 'Entrez le type de donnée souhaitée parmi mono, oligo ou poly : ' Type
read -p 'Entrez la longueur de séquences souhaitées parmi CDR3 ou Ent : ' long


if [ "$algo" = "Louvain" ]
then
	export ALGO="$PWD/algoCluster/$algo/LouvainClustering.py"
	export RESULT="$PWD/algoCluster/$algo/results/$Type""clonal_simp_indel_cdr3.txt"
fi

if [ "$algo" = "SpectralClustering" ]
then
        export ALGO="$PWD/algoCluster/$algo/SpectralClustering.py"
	export RESULT="$PWD/algoCluster/$algo/results/$Type""clonal_simp_indel_cdr3.txt"
fi




if [ "$long" = "Ent" ]
then
	export DATA="$PWD/data/Artificial/EntireSeq/$Type""clonal_simp_indel_cdr3.fa"
fi

if [ "$long" = "CDR3" ]
then
	export DATA="$PWD/data/Artificial/Extracted_CDR3/$Type""clonal_simp_indel_cdr3.fa"
fi




export F1="$PWD/evaluation/F1-score/cluster_based_fscore.py"
export SILHOUETTE="$PWD/evaluation/Silhouette/Silhouette.py"
export TIME="$PWD/evaluation/Exec_time/Exec_time.py"
export RECALL="$PWD/evaluation/Analysis-Recall/analysis-recall.py"
export GRAPH="$PWD/evaluation/Visualisation/show-graph.py"
export ANALYSIS="$PWD/evaluation/Analysis-Recall/essai2.py"
export TESTBENCH="$PWD/algoCluster/Test_Bench/test_bench.py"
export REF="$PWD/data/Artificial/True_clusters/$Type""clonal_simp_indel_true_clusters.txt"
export RESIMGT="$PWD/data/Tools_output/IMGT_output/Simulated_data/$Type""_simp_indel_imgt_Fo.txt"
