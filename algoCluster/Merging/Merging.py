#! /usr/bin/env python3
# coding: utf-8
import os
import sys
import networkx as nx
pwd = os.getcwd()
sys.path.append(pwd+'/tool') # Fonctionne sur windows et linux, et permet d'indiquer dans quel fichier sont les modules. 
import argparse
import community ###### ALGO DE LOUVAIN #######
import consensus
#import graph_input 
import result_output

###############################################################
#  Permet de calculer la taille d'un graphe network x
###############################################################

def size_nx(G):
	res = 0
	for e in G.edges(data=True):
		res += sys.getsizeof(e)
	for n in G.nodes(data=True):
		res += sys.getsizeof(n)
	return res


##############################################################
#   Début du code 
##############################################################

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-p","--patient",help="""type de patient à utiliser""")
	parser.add_argument("-r","--result",help="""nom du fichier résultat, qui sera dans le dossier de l'algo""")
	return parser.parse_args()

#############################################################
#   Appelé par le module TIME
#############################################################

def exec(path_to_file): # utilisé par Exec_Time pour timer l'algo
	dico_des_graphes, dico_init = graph_input.generate_graphs_and_init(path_to_file)
	
	partitions = {}
	for w in dico_des_graphes.keys():
		partitions[w] = community.best_partition(dico_des_graphes[w], dico_init[w])
	return 0


############################################################
#              MAIN
############################################################

def main():
	args = parse_arguments()
	patient = args.patient
	result = args.result
	path_to_file = "/home/lisa/Programmation/cloneCluster/data/Tools_output/IMGT_output/Simulated_data/"+ patient+ "_simp_indel_imgt_Fo.txt"
	path_to_data = "/home/lisa/Programmation/cloneCluster/data/Artificial/Extracted_CDR3/" + patient+"clonal_simp_indel_cdr3.fa"
	path_to_result = "/home/lisa/Programmation/cloneCluster/algoCluster/Merging/" + result+".txt"
	
	dico_des_graphes = consensus.generate_graphs_consensus(path_to_file,path_to_data)
	print("dico des graphes : ", dico_des_graphes)
	partitions = {}
	
	for w in dico_des_graphes.keys():
		partitions[w] = community.best_partition(dico_des_graphes[w])
	
	result_output.generate_output_text(partitions,path_to_result) #permet de générer le fichier texte qui ensuite sert à comparer les résultats aux true clusters


if __name__ == "__main__": 
	main()
