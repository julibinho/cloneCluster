#! /usr/bin/env python3
# coding: utf-8

import os
import sys

pwd = os.getcwd()
sys.path.append(pwd+'/tool')

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

chemin_EntireSeq = {'mono' : pwd+'/data/Real/EntireSeq/I3_mono.fa', 
		    'oligo': pwd+'/data/Real/EntireSeq/I1_oligo.fa',
		    'poly' : pwd+'/data/Real/EntireSeq/I4_poly.fa'}
		    
result_EntireSeq = {'mono' : pwd+'/result/Real/EntireSeq/I3_mono.txt', 
		    'oligo': pwd+'/result/Real/EntireSeq/I1_oligo.txt',
		    'poly' : pwd+'/result/Real/EntireSeq/I4_poly.txt'}
		    
		    

chemin_CDR3 = {'mono' : pwd+'/data/Real/Extracted_CDR3/P3_CDR3_mono.fa', 
	       'oligo': pwd+'/data/Real/Extracted_CDR3/P1_CDR3_oligo.fa',
	       'poly' : pwd+'/data/Real/Extracted_CDR3/P4_CDR3_poly.fa'}
	       
result_CDR3 = {'mono' : pwd+'/result/Real/Extracted_CDR3/P3_CDR3_mono.fa', 
	       'oligo': pwd+'/result/Real/Extracted_CDR3/P1_CDR3_oligo.fa',
	       'poly' : pwd+'/result/Real/Extracted_CDR3/P4_CDR3_poly.fa'}

###########################################################################
#training : 
chemin_EntireSeq = {'mono' : pwd+'data/Artificial/EntireSeq/monoclonal_simp_indel.fa', 
		    'oligo': pwd+'data/Artificial/EntireSeq/oligoclonal_simp_indel.fa',
		    'poly' : pwd+'data/Artificial/EntireSeq/polyclonal_simp_indel.fa'}
		    
result_EntireSeq = {'mono' : pwd+'/result/Artificial/EntireSeq/monoclonal_simp_indel.txt', 
		    'oligo': pwd+'/result/Artificial/EntireSeq/oligoclonal_simp_indel.txt',
		    'poly' : pwd+'/result/Artificial/EntireSeq/polyclonal_simp_indel.txt'}




chemin_CDR3 = {'mono' : pwd+'/data/Artificial/Extracted_CDR3/monoclonal_simp_indel_cdr3.fa', 
	       'oligo': pwd+'/data/Artificial/Extracted_CDR3/oligoclonal_simp_indel_cdr3.fa',
	       'poly' : pwd+'/data/Artificial/Extracted_CDR3/polyclonal_simp_indel_cdr3.fa'}
	       
result_CDR3 = {'mono' : pwd+'/result/Artificial/Extracted_CDR3/monoclonal_simp_indel_cdr3.txt', 
	       'oligo': pwd+'/result/Artificial/Extracted_CDR3/oligoclonal_simp_indel_cdr3.txt',
	       'poly' : pwd+'/result/Artificial/Extracted_CDR3/polyclonal_simp_indel_cdr3.txt'}

	       
data = ['mono','oligo','poly']	       

##############################################################################


def main():
	text_markdown = ''  #le but est de présenter un tableau au format markdown
	
	
	for ty in data:
		text_markdown += '## Patient ' + ty + 'clonal\n' + '| Type de séquence | Temps d\'execution | Silhouette | VJerror | Nombres de clusters trouvés | \n | ---------------- | ----------------- | ---------- | ------- | --------------------------- |\n'
		
		################ CDR3 ##########################
		dico_des_graphes = graph_input.generate_graphs(chemin_CDR3[ty])
		print('le graphe des séquence pour les CDR3 des données de ', ty,' est construit, l\'algo commence à réunir les clusters')
		partition = {}
		for w in dico_des_graphes.keys():
			partition[w] = community.best_partition(dico_des_graphes[w])
		result_output.generate_output_text(partition, result_CDR3[ty])
		
		
		
 

if __name__ == "__main__":
	main()


