#! /usr/bin/env python3
# coding: utf-8

import os
import sys

pwd = os.getcwd()
sys.path.append(pwd+'/utils')

sys.path.append(pwd+'/evaluation/Silhouette')
sys.path.append(pwd+'/evaluation/Exec_time')
sys.path.append(pwd+'/evaluation/VJerror') # les fichiers à passer en entrée sont dans data/Real/VJ_file/

import argparse
import community ###### ALGO DE LOUVAIN #######
#import affichage

import graph_input 
import result_output

import Silhouette
import Exec_time
import VJerror

chemin_VJ = {'mono' : pwd+'/data/Real/VJ_file/I3_VDJ_mono.txt', 
	     'oligo': pwd+'/data/Real/VJ_file/I1_VDJ_oligo.txt',
	     'poly' : pwd+'/data/Real/VJ_file/I4_VDJ_poly.txt'}

chemin_entierSeq = {'mono' : pwd+'/data/Real/entierSeq/I3_mono.fa', 
		    'oligo': pwd+'/data/Real/entierSeq/I1_oligo.fa',
		    'poly' : pwd+'/data/Real/entierSeq/I4_poly.fa'}

chemin_CDR3 = {'mono' : pwd+'/data/Real/Extracted_CDR3/P3_CDR3_mono.fa', 
	       'oligo': pwd+'/data/Real/Extracted_CDR3/P1_CDR3_oligo.fa',
	       'poly' : pwd+'/data/Real/Extracted_CDR3/P4_CDR3_poly.fa'}

###########################################################################
#training : 
chemin_entierSeq = {'mono' : pwd+'/data/artficial/entireSeq/monoclonal_simp_indel.fasta', 
		    'oligo': pwd+'/data/artficial/entireSeq/oligoclonal_simp_indel.fasta',
		    'poly' : pwd+'/data/artficial/entireSeq/polyclonal_simp_indel.fasta'}

chemin_CDR3 = {'mono' : pwd+'/data/artficial/Extracted_CDR3/monoclonal_simp_indel_cdr3.fa', 
	       'oligo': pwd+'/data/artficial/Extracted_CDR3/oligoclonal_simp_indel_cdr3.fa',
	       'poly' : pwd+'/data/artficial/Extracted_CDR3/polyclonal_simp_indel_cdr3.fa'}

	       
data = ['mono','oligo','poly']	       

##############################################################################


def main():
	fichier_sortie = '| Type de patient | Type de séquence | Temps d\'execution | Silhouette | VJerror | Nombres de clusters trouvés | \n | ---------------- | ----------------- | ---------- | ------- | --------------------------- |\n' #le but est de présenter un tableau au format markdown
	
	
	for ty in data:
		graph_input.generate_graphs(chemin_CDR3[ty])
		print('le graphe des séquence pour les CDR3 des données de ', ty,' est construit, l\'algo commence à réunir les clusters')
 

if __name__ == "__main__":
	main()


