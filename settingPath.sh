#!/bin/bash

#export 

#read -p 'Quel fichier souhaitez vous utiliser ? ' fichier
#DATA="data/artficial/Extracted_CDR3/$fichier.fa"

read -p 'Entrez l algorithme que vous souhaitez utiliser parmis Louvain ou SpectralClustering : ' algo 
read -p 'Entrez le type de donnée souhaitée parmi mono, oligo ou poly : ' Type
read -p 'Entrez la longueur de séquences souhaitées parmi CDR3 ou EntireSeq : ' long
read -p 'Entrez la caractéristique des données souhaitées parmi Artificial ou Real : ' caract


if [ "$algo" = "Louvain" ]
then
	export ALGO="$PWD/algoCluster/$algo/LouvainClustering.py"
fi

if [ "$algo" = "SpectralClustering" ]
then
    export ALGO="$PWD/algoCluster/$algo/SpectralClustering.py"
fi


if [ "$caract" = "Artificial" ]
then

    if [ "$long" = "Ent" ]
    then
	    export DATA="$PWD/data/$caract/EntireSeq/$Type""clonal_simp_indel.fa"
	    export RESULT="$PWD/result/$caract/$algo/EntireSeq/$Type""clonal_simp_indel.txt"
    fi

    if [ "$long" = "CDR3" ]
    then
	    export DATA="$PWD/data/$caract""/Extracted_CDR3/$Type""clonal_simp_indel_cdr3.fa"
	    export RESULT="$PWD/result/$caract""/$algo/CDR3/$Type""clonal_simp_indel_cdr3.txt"
    fi
fi

if [ "$caract" = "Real" ]
then
    if [ "$long" = "Ent" ]
    then
        if [ "$Type" = "mono" ]
        then
            export DATA="$PWD/data/$caract/EntireSeq/I3_mono.fa"
	        export RESULT="$PWD/result/$caract/$algo/EntireSeq/$Type""clonal_simp_indel.txt"
	    fi
	    if [ "$Type" = "oligo" ]
        then
            export DATA="$PWD/data/$caract/EntireSeq/I1_oligo.fa"
	        export RESULT="$PWD/result/$caract/$algo/EntireSeq/$Type""clonal_simp_indel.txt"
	    fi
	    if [ "$Type" = "poly" ]
        then
            export DATA="$PWD/data/$caract/EntireSeq/I4_poly.fa"
	        export RESULT="$PWD/result/$caract/$algo/EntireSeq/$Type""clonal_simp_indel.txt"
	    fi
    fi

    if [ "$long" = "CDR3" ]
    then
        if [ "$Type" = "mono" ]
        then
            export DATA="$PWD/data/$Caract/Extracted_CDR3/I3_CDR3_mono.fa"
	        export RESULT="$PWD/result/$caract/$algo/CDR3/$Type""clonal_simp_indel_cdr3.txt"
	    fi
	    if [ "$Type" = "oligo" ]
        then
            export DATA="$PWD/data/$Caract/Extracted_CDR3/I1_CDR3_oligo.fa"
	        export RESULT="$PWD/result/$caract/$algo/CDR3/$Type""clonal_simp_indel_cdr3.txt"
	    fi
	    if [ "$Type" = "poly" ]
        then
            export DATA="$PWD/data/$Caract/Extracted_CDR3/I4_CDR3_poly.fa"
	        export RESULT="$PWD/result/$caract/$algo/CDR3/$Type""clonal_simp_indel_cdr3.txt"
	    fi
    fi
fi

#Les algos : 

export F1="$PWD/evaluation/F1-score/cluster_based_fscore.py"
export SILHOUETTE="$PWD/evaluation/Silhouette/Silhouette.py"
export TIME="$PWD/evaluation/Exec_time/Exec_time.py"
export RECALL="$PWD/evaluation/Analysis-Recall/analysis-recall.py"
export GRAPH="$PWD/evaluation/Visualisation/show-graph.py"
export ANALYSIS="$PWD/evaluation/Analysis-Recall/essai2.py"
export TESTBENCH="$PWD/algoCluster/Test_Bench/test_bench.py"
export REF="$PWD/data/Artificial/True_clusters/$Type""clonal_simp_indel_true_clusters.txt"
export CLUST_IMGT="$PWD/data/Tools_output/IMGT_output/Simulated_data/$Type""_simp_indel_imgt_Fo.txt"
export MERG="$PWD/algoCluster/Merging/Merging.py"
export REF_IMGT="$PWD/data/Artificial/Extracted_CDR3/$Type""clonal_simp_indel_cdr3.fa"
export RES_IMGT="$PWD/result/Merging/Artificial/$Type""_merging_clonal_simp_indel_cdr3.txt"














