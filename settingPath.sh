#!/bin/bash

#export 

#read -p 'Quel fichier souhaitez vous utiliser ? ' fichier
#DATA="data/artficial/Extracted_CDR3/$fichier.fa"

read -p 'Entrez l algorithme que vous souhaitez utiliser parmis Louvain (l), SpectralClustering (s), Gclust (g) ou un merging sur les données IMGT (m) : ' algo 

##################################### LOUVAIN #########################################
if [ "$algo" = "l" ]
then
    algo="Louvain"
    export ALGO="$PWD/algoCluster/$algo/LouvainClustering.py"
    echo $algo
    read -p 'Entrez le type de patient à étudier : monoclonal (m), oligoclonal (o), ou polyclonal (p) : ' patient
    if [ "$patient" = "m" ]
    then
        patient="mono"
    fi
    if [ "$patient" = "o" ]
    then
        patient="oligo"
    fi
    if [ "$patient" = "p" ]
    then
        patient="poly"
    fi
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
            echo $patient
            if [ "$patient" = "mono" ] #monoclonal
            then
                export DATA="$PWD/data/Real/EntireSeq/I3_mono.fa"
	            export RESULT="$PWD/result/Real/$algo/EntireSeq/I3_$patient""clonal_simp_indel.txt"
	        fi
	        if [ "$patient" = "oligo" ] #oligo clonal
            then
                export DATA="$PWD/data/Real/EntireSeq/I1_oligo.fa"
	            export RESULT="$PWD/result/Real/$algo/EntireSeq/I1_$patient""clonal_simp_indel.txt"
	        fi
	        if [ "$patient" = "poly" ] #polyclonal
            then
                export DATA="$PWD/data/Real/EntireSeq/I4_poly.fa"
	            export RESULT="$PWD/result/Real/$algo/EntireSeq/I4_$patient""clonal_simp_indel.txt"
	        fi
        fi

        if [ "$long" = "c" ] #CDR3
        then
            echo $patient
            if [ "$patient" = "mono" ] #monoclonal
            then
                export DATA="$PWD/data/Real/Extracted_CDR3/I3_CDR3_mono.fa"
	            export RESULT="$PWD/result/Real/$algo/CDR3/I3_$patient""clonal_simp_indel_cdr3.txt"
	        fi
	        if [ "$patient" = "oligo" ] #oligoclonal
            then
                export DATA="$PWD/data/Real/Extracted_CDR3/I1_CDR3_oligo.fa"
	            export RESULT="$PWD/result/Real/$algo/CDR3/I1_$patient""clonal_simp_indel_cdr3.txt"
	        fi
	        if [ "$patient" = "poly" ] #polyclonal
            then
                export DATA="$PWD/data/Real/Extracted_CDR3/I4_CDR3_poly.fa"
	            export RESULT="$PWD/result/Real/$algo/CDR3/I4_$patient""clonal_simp_indel_cdr3.txt"
	        fi
        fi
    fi
fi

##################################### SPECTRAL CLUSTERING ########################################
if [ "$algo" = "s" ]
then
    algo="SpectralClustering"
    export ALGO="$PWD/algoCluster/$algo/SpectralClustering.py"
    read -p 'Entrez le type de patient à étudier : monoclonal (m), oligoclonal (o), ou polyclonal (p) : ' patient
    if [ "$patient" = "m" ]
    then
        patient="mono"
    fi
    if [ "$patient" = "o" ]
    then
        patient="oligo"
    fi
    if [ "$patient" = "p" ]
    then
        patient="poly"
    fi
    read -p 'Entrez le type de données à utiliser : réelles (r) ou artificielles (a) : ' caract
    read -p 'Entrez la longueur des séquences à utiliser : séquences entières (e) ou CDR3 (c) : ' long
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
	        export RESULT="$PWD/result/Artificial/$algo/CDR3/$patient""clonal_simp_indel_cdr3.txt"
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
	            export RESULT="$PWD/result/Real/$algo/EntireSeq/I3_$patient""clonal_simp_indel.txt"
	        fi
	        if [ "$patient" = "oligo" ] #oligo clonal
            then
                export DATA="$PWD/data/Real/EntireSeq/I1_oligo.fa"
	            export RESULT="$PWD/result/Real/$algo/EntireSeq/I1_$patient""clonal_simp_indel.txt"
	        fi
	        if [ "$patient" = "poly" ] #polyclonal
            then
                export DATA="$PWD/data/Real/EntireSeq/I4_poly.fa"
	            export RESULT="$PWD/result/Real/$algo/EntireSeq/I4_$patient""clonal_simp_indel.txt"
	        fi
        fi

        if [ "$long" = "c" ] #CDR3
        then
            if [ "$patient" = "mono" ] #monoclonal
            then
                export DATA="$PWD/data/Real/Extracted_CDR3/I3_CDR3_mono.fa"
	            export RESULT="$PWD/result/Real/$algo/CDR3/I3_$patient""clonal_simp_indel_cdr3.txt"
	        fi
	        if [ "$patient" = "oligo" ] #oligoclonal
            then
                export DATA="$PWD/data/Real/Extracted_CDR3/I1_CDR3_oligo.fa"
	            export RESULT="$PWD/result/Real/$algo/CDR3/I1_$patient""clonal_simp_indel_cdr3.txt"
	        fi
	        if [ "$patient" = "poly" ] #polyclonal
            then
                export DATA="$PWD/data/Real/Extracted_CDR3/I4_CDR3_poly.fa"
	            export RESULT="$PWD/result/Real/$algo/CDR3/I4_$patient""clonal_simp_indel_cdr3.txt"
	        fi
        fi
    fi
fi

######################################## MERGING ########################################################################### 
if [ "$algo" = "m" ]
then
    read -p 'Entrez le type de merging à utiliser : sur séquences consensus (c) ou sur profile (p) : ' merg
    if [ "$merg" = "c" ]
    then
        merg=consensus
    fi
    if [ "$merg" = "p" ]
    then
        merg=profile
    fi
    export ALGO="$PWD/algoCluster/Merging/Merging_$merg.py"
    read -p 'Entrez le type de données à utiliser : réelles (r) ou artificielles (a) : ' caract
    if [ "$caract" = "a" ] #données artificielles
    then
        read -p 'Entrez le type de patient à étudier : monoclonal (m), oligoclonal (o), ou polyclonal (p) : ' patient
        export F1="$PWD/evaluation/F1-score/cluster_based_fscore.py"
        export SILHOUETTE="$PWD/evaluation/Silhouette/Silhouette.py"
        export TIME="$PWD/evaluation/Exec_time/Exec_time.py"
        export RECALL="$PWD/evaluation/Analysis-Recall/analysis-recall.py"
        export GRAPH="$PWD/evaluation/Visualisation/show-graph.py"
        export ANALYSIS="$PWD/evaluation/Analysis-Recall/essai2.py"
        if [ "$patient" = "m" ]
        then
            export REF="$PWD/data/Artificial/True_clusters/monoclonal_simp_indel_true_clusters.txt"
        
            export CLUST="$PWD/data/Tools_output/IMGT_output/Simulated_data/mono_simp_indel_imgt_Fo.txt"
            export DATA="$PWD/data/Artificial/Extracted_CDR3/IMGT/mono_simu_6_Junction_CDR3_NA.txt"
            export RESULT="$PWD/result/Merging/Artificial/mono_merging_$merg""_IMGT_cdr3.txt"
	    fi
	    if [ "$patient" = "o" ]
        then
            export REF="$PWD/data/Artificial/True_clusters/oligoclonal_simp_indel_true_clusters.txt"
        
            export CLUST="$PWD/data/Tools_output/IMGT_output/Simulated_data/oligo_simp_indel_imgt_Fo.txt"
            export DATA="$PWD/data/Artificial/Extracted_CDR3/IMGT/oligo_simu_6_Junction_CDR3_NA.txt"
            export RESULT="$PWD/result/Merging/Artificial/oligo_merging_$merg""_IMGT_cdr3.txt"
	    fi
	    if [ "$patient" = "p" ]
        then
            export REF="$PWD/data/Artificial/True_clusters/polyclonal_simp_indel_true_clusters.txt"
        
            export CLUST="$PWD/data/Tools_output/IMGT_output/Simulated_data/poly_simp_indel_imgt_Fo.txt"
            export DATA="$PWD/data/Artificial/Extracted_CDR3/IMGT/poly_simu_6_Junction_CDR3_NA.txt"
            export RESULT="$PWD/result/Merging/Artificial/poly_merging_$merg""_IMGT_cdr3.txt"
	    fi

    fi

    if [ "$caract" = "r" ] #données réelles
    then
        read -p 'Numéro du patient (1, 3 ou 4) : ' patient
        export SILHOUETTE="$PWD/evaluation/Silhouette/Silhouette.py"
        export TIME="$PWD/evaluation/Exec_time/Exec_time.py"
        
        export CLUST="$PWD/data/Tools_output/IMGT_output/Real_data/I$patient""_IMGT_Fo_cleaned.txt"
        export DATA="$PWD/data/Real/Extracted_CDR3/Extracted_by_IMGT/I$patient""_CDR3_NA.txt"
        export RESULT="$PWD/result/Merging/Real/I$patient""_merging_$merg""_IMGT_cdr3.txt"
        
    fi
fi
    
#################################### GCLUST ###############################################
if [ "$algo" = "g" ]
then
    algo="Gclust"
    export ALGO="$PWD/algoCluster/$algo/gclust.py"
    read -p 'Entrez le type de patient à étudier : monoclonal (m), oligoclonal (o), ou polyclonal (p) : ' patient
    if [ "$patient" = "m" ]
    then
        patient="mono"
    fi
    if [ "$patient" = "o" ]
    then
        patient="oligo"
    fi
    if [ "$patient" = "p" ]
    then
        patient="poly"
    fi
    read -p 'Entrez le type de données à utiliser : réelles (r) ou artificielles (a) : ' caract
    read -p 'Entrez la longueur des séquences à utiliser : séquences entières (e) ou CDR3 (c) : ' long
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
	        export RESULT="$PWD/result/Artificial/$algo/EntireSeq/$patient""clonal_simp_indel_cdr3.fa_Resultats_GClustering.txt"
            export RESULT_INTER="$PWD/result/Artificial/$algo/EntireSeq/Clustering.txt"
            
        fi

        if [ "$long" = "c" ] #CDR3
        then
	        export DATA="$PWD/data/Artificial/Extracted_CDR3/Vidjil/$patient""clonal_simp_indel_cdr3.fa"
	        export RESULT="$PWD/result/Artificial/$algo/CDR3/$patient""clonal_simp_indel_cdr3.fa_Resultats_GClustering.txt"
            export RESULT_INTER="$PWD/result/Artificial/$algo/CDR3/Clustering.txt"
            export DATA_IMGT="$PWD/data/Artificial/Extracted_CDR3/IMGT/$patient""_simu_6_Junction_CDR3_NA.txt"
            export REF_IMGT="$PWD/data/Tools_output/IMGT_output/Simulated_data/$patient""_simp_indel_imgt_Fo.txt"
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
	            export RESULT="$PWD/result/Real/$algo/EntireSeq/I3_$patient""clonal_simp_indel.txt"
	        fi
	        if [ "$patient" = "oligo" ] #oligo clonal
            then
                export DATA="$PWD/data/Real/EntireSeq/I1_oligo.fa"
	            export RESULT="$PWD/result/Real/$algo/EntireSeq/I1_$patient""clonal_simp_indel.txt"
	        fi
	        if [ "$patient" = "poly" ] #polyclonal
            then
                export DATA="$PWD/data/Real/EntireSeq/I4_poly.fa"
	            export RESULT="$PWD/result/Real/$algo/EntireSeq/I4_$patient""clonal_simp_indel.txt"
	        fi
        fi

        if [ "$long" = "c" ] #CDR3
        then
            if [ "$patient" = "mono" ] #monoclonal
            then
                export DATA="$PWD/data/Real/Extracted_CDR3/I3_CDR3_mono.fa"
	            export RESULT="$PWD/result/Real/$algo/CDR3/I3_$patient""clonal_simp_indel_cdr3.txt"
	        fi
	        if [ "$patient" = "oligo" ] #oligoclonal
            then
                export DATA="$PWD/data/Real/Extracted_CDR3/I1_CDR3_oligo.fa"
	            export RESULT="$PWD/result/Real/$algo/CDR3/I1_$patient""clonal_simp_indel_cdr3.txt"
	        fi
	        if [ "$patient" = "poly" ] #polyclonal
            then
                export DATA="$PWD/data/Real/Extracted_CDR3/I4_CDR3_poly.fa"
	            export RESULT="$PWD/result/Real/$algo/CDR3/I4_$patient""clonal_simp_indel_cdr3.txt"
	        fi
        fi
    fi
fi