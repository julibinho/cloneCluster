#! /usr/bin/env python3
# coding: utf-8
import os
import argparse
import community
import networkx as nx
import matplotlib.pyplot as plt
import utils.louvain as l
import utils.affichage
import utils.formatage as fr
###################################
import utils.tri_des_seq as tri
import utils.matrice_distance_hamming as matHamming

def parse_arguments():
	parser = argparse.ArgumentParser()
	#parser.add_argument("-e", "--extension", help="""Quelle extension a le fichier ?""")
	#parser.add_argument("-d","--datafile",help="""Quel fichier Fasta souhaite-t-on analyser ?""")
	parser.add_argument("-p","--path_to_file",help="""Chemin vers le fichier à utiliser""")
	parser.add_argument("-s","--size",help="""Quel graphe de cluster souhaite-t-on afficher ?""")
	return parser.parse_args()

def main():
	args = parse_arguments()
	path_to_file = args.path_to_file
	#size = int(args.size)
	#dico_des_sequences = tri.tri(path_to_file)
	#dico_des_matrices = matHamming.matrices(dico_des_sequences)
	
	
	dico_des_sequences = tri.tri_cle_valeur(path_to_file) #trie les séquences par tailles
	dico_des_graphes = matHamming.instanciation_des_graphes_cle_valeur(dico_des_sequences) # crée les graphes de distances
	#affichage.affiche_G_avec_poids(dico_des_graphes[size])
	partitions = l.cluster_louvain(dico_des_graphes) # renvoie un dictionnaire contenant les partitions par tailles
	#l.print_louvain(partitions[size]) 
	fr.formatage(partitions)


if __name__ == "__main__": 
	main()
