#! /usr/bin/env python3
# coding: utf-8
import os
import sys

pwd = os.getcwd()
sys.path.append(pwd+'/utils') # Fonctionne sur windows et linux (normalement), et permet d'indiquer dans quel fichier sont les modules. 


import argparse
import community
import networkx as nx
#import matplotlib.pyplot as plt
import louvain as l
import affichage
import formatage as fr
import tri_des_seq as tri
import matrice_distance_hamming as matHamming

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-p","--path_to_file",help="""Chemin vers le fichier à utiliser""")
	parser.add_argument("-s","--size",help="""Quel graphe de cluster souhaite-t-on afficher ?""")
	parser.add_argument("-r","--result",help="""Ou doit-on ranger le résultat ?""")
	return parser.parse_args()

def main():
	args = parse_arguments()
	path_to_file = args.path_to_file
	path_to_result = args.result
	#size = int(args.size)
	
	
	dico_des_sequences = tri.tri_cle_valeur(path_to_file) #trie les séquences par tailles
	
	
	dico_des_graphes = matHamming.instanciation_des_graphes_cle_valeur(dico_des_sequences) # crée les graphes de distances
	
	
	partitions = l.cluster_louvain(dico_des_graphes) # renvoie un dictionnaire contenant les partitions par tailles
	
	
	fr.formatage(partitions,path_to_result) #permet de générer le fichier texte qui ensuite sert à comparer les résultats aux true clusters


if __name__ == "__main__": 
	main()
