#!/bin/bash

for patient in "mono" "oligo" "poly"
do
    algo="Louvain"
    export ALGO="$PWD/algoCluster/$algo/LouvainClustering.py"
    #echo $algo
    #read -p 'Entrez le type de patient à étudier : monoclonal (m), oligoclonal (o), ou polyclonal (p) : ' patient
    read -p 'Entrez le type de données à utiliser : réelles (r) ou artificielles (a) : ' caract
    read -p 'Entrez la longueur des séquences à utiliser : séquences entières (e), CDR3 (c), ou CDR3 d IMGT (i) : ' long
    if [ "$caract" = "a" ] #données artificielles
    then
        export F1="$PWD/evaluation/F1-score/cluster_based_fscore.py"
        export SILHOUETTE="$PWD/evaluation/Silhouette/Silhouette.py"
        export TIME="$PWD/evaluation/Exec_time/Exec_time.py"
        export RECALL="$PWD/evaluation/Analysis-Recall/analysis-recall.py"
        export GRAPH="$PWD/evaluation/Visualisation/show-graph.py"
        export ANALYSIS="$PWD/evaluation/Analysis-Recall/essai2.py"
        export REF="$PWD/data/Artificial/True_clusters/$patient""clonal_simp_indel_true_clusters.txt"
        
        if [ "$long" = "e" ] #séquences entières
        then
	        export DATA="$PWD/data/Artificial/EntireSeq/$patient""clonal_simp_indel.fa"
	        export RESULT="$PWD/result/Artificial/$algo/EntireSeq/$patient""clonal_simp_indel.txt"
        fi

        if [ "$long" = "c" ] #CDR3
        then
	        export DATA="$PWD/data/Artificial/Extracted_CDR3/Vidjil/$patient""clonal_simp_indel_cdr3.fa"
	        export RESULT="$PWD/result/Artificial/$algo/CDR3/$patient""clonal_simp_indel_extracted_cdr3.txt"
        fi
        if [ "$long" = "i" ]
        then
            export DATA="$PWD/data/Artificial/Extracted_CDR3/IMGT/$patient""_simu_6_Junction_CDR3_NA.txt"
	        export RESULT="$PWD/result/Artificial/$algo/CDR3/$patient""clonal_simp_indel_IMGT_cdr3.txt"
	    fi
    fi

    if [ "$caract" = "r" ] #données réelles
    then
        export SILHOUETTE="$PWD/evaluation/Silhouette/Silhouette.py"
        export TIME="$PWD/evaluation/Exec_time/Exec_time.py"
        if [ "$long" = "e" ] #séquences entières
        then
            if [ "$patient" = "mono" ] #monoclonal
            then
                export DATA="$PWD/data/Real/EntireSeq/I3_mono.fa"
	            export RESULT="$PWD/result/Real/$algo/EntireSeq/$patient""clonal_simp_indel.txt"
	        fi
	        if [ "$patient" = "oligo" ] #oligo clonal
            then
                export DATA="$PWD/data/Real/EntireSeq/I1_oligo.fa"
	            export RESULT="$PWD/result/Real/$algo/EntireSeq/$patient""clonal_simp_indel.txt"
	        fi
	        if [ "$patient" = "poly" ] #polyclonal
            then
                export DATA="$PWD/data/Real/EntireSeq/I4_poly.fa"
	            export RESULT="$PWD/result/Real/$algo/EntireSeq/$patient""clonal_simp_indel.txt"
	        fi
        fi

        if [ "$long" = "c" ] #CDR3
        then
            if [ "$patient" = "m" ] #monoclonal
            then
                export DATA="$PWD/data/Real/Extracted_CDR3/I3_CDR3_mono.fa"
	            export RESULT="$PWD/result/Real/$algo/CDR3/$patient""clonal_simp_indel_cdr3.txt"
	        fi
	        if [ "$patient" = "o" ] #oligoclonal
            then
                export DATA="$PWD/data/Real/Extracted_CDR3/I1_CDR3_oligo.fa"
	            export RESULT="$PWD/result/Real/$algo/CDR3/$patient""clonal_simp_indel_cdr3.txt"
	        fi
	        if [ "$patient" = "p" ] #polyclonal
            then
                export DATA="$PWD/data/Real/Extracted_CDR3/I4_CDR3_poly.fa"
	            export RESULT="$PWD/result/Real/$algo/CDR3/$patient""clonal_simp_indel_cdr3.txt"
	        fi
        fi
    fi
done

#IFS=$'\n' read -r -d '' -a my_array < <( my_command && printf '\0' )
