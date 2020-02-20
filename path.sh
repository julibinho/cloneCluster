#!/bin/bash

#export 

#read -p 'Quel fichier souhaitez vous utiliser ? ' fichier
#DATA="data/artficial/Extracted_CDR3/$fichier.fa"

read -p 'Entez le type de donnée souhaitée parmi mono, oligo ou poly : ' type

export DATA="$PWD/data/artficial/Extracted_CDR3/$type""clonal_simp_indel_cdr3.fa"
export DATAENT="$PWD/data/artficial/entireSeq/$type""clonal_simp_indel.fasta"
#echo $DATA
#echo DATA=data/artficial/Extracted_CDR3/oligoclonal_simp_indel_cdr3.fa 
#echo $DATA
export ALGO="$PWD/algoCluster/Louvain/clustering.py"
export RESULT="$PWD/algoCluster/Louvain/results/res.txt"
export REF="$PWD/data/artficial/True_clusters/$type""clonal_simp_indel_true_clusters.txt"
export F1="$PWD/evaluation/F1-score/Evaluate_Sim_Cluster.py"
export SILHOUETTE="$PWD/evaluation/Silhouette/Silhouette.py"
export TIME="$PWD/evaluation/Exec-Time/Exec-time.py"
#export FASTAFILE="$PWD/data/artficial/True_clusters/$type""clonal_simp_indel_true_clusters.txt"
