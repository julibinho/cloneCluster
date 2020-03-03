#! /usr/bin/env python3
# coding: utf-8
import os
import sys

pwd = os.getcwd()
sys.path.append(pwd+'/utils') # Fonctionne sur windows et linux, et permet d'indiquer dans quel fichier sont les modules. 

import argparse
import community ###### ALGO DE LOUVAIN #######
#import affichage

import graph_input 
import result_output



def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-p","--path_to_file",help="""Chemin vers le fichier à utiliser""")
	parser.add_argument("-r","--result",help="""Ou doit-on ranger le résultat ?""")
	return parser.parse_args()



def main():
	args = parse_arguments()
	path_to_file = args.path_to_file
	path_to_result = args.result
	#size = int(args.size)
	
	dico_des_graphes = graph_input.generate_graphs(path_to_file)
	
	partitions = {}
	for w in dico_des_graphes.keys():
		partitions[w] = community.best_partition(dico_des_graphes[w])
	result_output.generate_output_text(partitions,path_to_result) #permet de générer le fichier texte qui ensuite sert à comparer les résultats aux true clusters


if __name__ == "__main__": 
	main()
