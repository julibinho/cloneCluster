#! /usr/bin/env python3
# coding: utf-8

import os
import sys
import time

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

import Silhouette as sil
import VJerror as vj

REAL = False

if REAL :

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
	       
	result_CDR3 = {'mono' : pwd+'/result/Real/Extracted_CDR3/P3_CDR3_mono.txt', 
		       'oligo': pwd+'/result/Real/Extracted_CDR3/P1_CDR3_oligo.txt',
		       'poly' : pwd+'/result/Real/Extracted_CDR3/P4_CDR3_poly.txt'}

###########################################################################
#training : 
else : 
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

	       
data = ['poly']#,'oligo','poly']	       

##############################################################################

def generate_one_graph(dico): # pour ne pas déborder la mémoire
	for c, v in dico.items():
		print('dans le for de generate one graph')
		cle = c 
		valeur = v
		break
	dico.pop(cle)
	return instanciation_des_graphes_cle_valeur({cle : valeur})



def main():
	text_markdown = ''  #le but est de présenter un tableau au format markdown
	if REAL :
		text_markdown += '# Résultat avec les données réelles\n'
	
	for type_seq in data:
		text_markdown += '## Patient ' + type_seq + 'clonal\n' + '| Type of sequences | Time (s) | Silhouette | VJerror | # of clusters | \n | :----------------: | :-----------------: | :----------: | :-------: | :---------------------------: |\n'
		
		################ CDR3 ##########################
		start_time = time.time()
		dico = graph_input.tri_cle_valeur(chemin_CDR3[type_seq]) # dico {longueur : {nom:seq}}
		partition = {}
		for cle, valeur in dico.items():
			print('séquences CDR3 de longueur : ', cle)
			graphe = graph_input.instanciation_des_graphes_cle_valeur({cle:valeur})
			partition[cle]=community.best_partition(graphe[cle])
		result_output.generate_output_text(partition, result_CDR3[type_seq])
		exec_time = time.time() - start_time

		
		 	################ Silhouette ######################
		print('calcul de la silhouette')
		FastaFile = chemin_CDR3[type_seq]
		ClusteringFile = result_CDR3[type_seq]
		Dicofasta=sil.readFastaMul(FastaFile)
		Dicoresult=sil.readClusteringResults(ClusteringFile)
		nb_cluster = len(Dicoresult)
		Dicocentroid=sil.CalculateMedoid(Dicofasta,Dicoresult)
		DicoNeighbour= sil.CalculateMedianDist(Dicocentroid)

		res_sil=sil.silhouette(Dicofasta,Dicocentroid,Dicoresult,DicoNeighbour)
		
			##################### VJerror #######################"
		if REAL :
			VJ_file = chemin_VJ[type_seq]
			tool_output = result_CDR3[type_seq]
			VJ_lines = vj.read_output_file(VJ_file)
			VJ_dico = vj.dico_VJ_format(VJ_lines)
			cluster_lines = vj.read_output_file(tool_output)
			dico_cluster_VJ = vj.creat_dico_cluster_VJ (VJ_dico, cluster_lines)
			VJ_er = vj.calculate_error(dico_cluster_VJ)
			name = 'result_Real_' + time.strftime("%d_%m_%Y__%Hh_%Mmin_%Ssec") + '.md'
		else :
			VJ_er = 0.98
			name = 'result_Artificial_' + time.strftime("%d_%m_%Y__%Hh_%Mmin_%Ssec") + '.md'
		
		
		
		text_markdown += '| CDR3 | %.5s | ' % exec_time +  ' %.5s | ' % res_sil + ' %.9s' %VJ_er +' | %s |\n' % nb_cluster
	
	with open(pwd + '/algoCluster/Test_Bench/result_markdown/' + name, "w") as fichier:
		fichier.write(text_markdown)
	fichier.close()
	print('fini')
		
 

if __name__ == "__main__":
	main()


