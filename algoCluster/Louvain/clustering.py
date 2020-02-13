#! /usr/bin/env python3
# coding: utf-8
import os
import sys
#sys.path.append('/home/lisa/Programmation/cloneCluster/utils') # *nix path
# équivalent de 'from modules import module', mais, pour le coup, dynamique
pwd = os.getcwd()
sys.path.append(pwd+'/utils') # *nix path
#print(sys.path)


import argparse
import community
import networkx as nx
import matplotlib.pyplot as plt
import louvain as l
import affichage
import formatage as fr
###################################
import tri_des_seq as tri
import matrice_distance_hamming as matHamming

def parse_arguments():
	parser = argparse.ArgumentParser()
	#parser.add_argument("-e", "--extension", help="""Quelle extension a le fichier ?""")
	#parser.add_argument("-d","--datafile",help="""Quel fichier Fasta souhaite-t-on analyser ?""")
	parser.add_argument("-p","--path_to_file",help="""Chemin vers le fichier à utiliser""")
	parser.add_argument("-s","--size",help="""Quel graphe de cluster souhaite-t-on afficher ?""")
	parser.add_argument("-r","--result",help="""Ou doit-on ranger le résultat ?""")
	return parser.parse_args()

def main():
	args = parse_arguments()
	path_to_file = args.path_to_file
	path_to_result = args.result
	#size = int(args.size)
	#dico_des_sequences = tri.tri(path_to_file)
	#dico_des_matrices = matHamming.matrices(dico_des_sequences)
	
	
	dico_des_sequences = tri.tri_cle_valeur(path_to_file) #trie les séquences par tailles
	#print("dans clustering", set(dico_des_sequences.keys()))
	dico_des_graphes = matHamming.instanciation_des_graphes_cle_valeur(dico_des_sequences) # crée les graphes de distances
	#affichage.affiche_G_avec_poids(dico_des_graphes[size])
	partitions = l.cluster_louvain(dico_des_graphes) # renvoie un dictionnaire contenant les partitions par tailles
	#l.print_louvain(partitions[size]) 
	fr.formatage(partitions,path_to_result)
	#print(partitions)


if __name__ == "__main__": 
	main()
