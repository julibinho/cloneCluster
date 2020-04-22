#! /usr/bin/env python3
# coding: utf-8
import os
import sys
import networkx as nx
pwd = os.getcwd()
sys.path.append(pwd+'/algoCluster/ToolGiveName') # Fonctionne sur windows et linux, et permet d'indiquer dans quel fichier sont les modules. 
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
	parser.add_argument("-c","--cluster_file",help="""résultat de l'algo""")
	parser.add_argument("-d","--data",help="""fasta avec les id et les séquences""")
	parser.add_argument("-r","--result",help="""ou ranger le resultat ? """)
	return parser.parse_args()

#############################################################
#   Appelé par le module TIME
#############################################################

def exec(path_to_file, path_to_data): # utilisé par Exec_Time pour timer l'algo
	dico_des_graphes = consensus.generate_graphs_consensus(path_to_file,path_to_data)
	partitions = {}
	
	for w in dico_des_graphes.keys():
		partitions[w] = community.best_partition(dico_des_graphes[w])
	return 0


############################################################
#              MAIN
############################################################

def main():
	args = parse_arguments()
	path_to_file = args.cluster_file
	path_to_data = args.data
	path_to_result = args.result
	dico_des_graphes = consensus.generate_graphs_consensus(path_to_file,path_to_data)
	partitions = {}
	
	for w in dico_des_graphes.keys():
		partitions[w] = community.best_partition(dico_des_graphes[w])
	
	result_output.generate_output_text(partitions,path_to_result) #permet de générer le fichier texte qui ensuite sert à comparer les résultats aux true clusters


if __name__ == "__main__": 
	main()
