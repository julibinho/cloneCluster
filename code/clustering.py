#! /usr/bin/env python3
# coding: utf-8
import os
import argparse
import tri_des_seq as tri
import matrice_distance_hamming as matHamming

def parse_arguments():
	parser = argparse.ArgumentParser()
	#parser.add_argument("-e", "--extension", help="""Quelle extension a le fichier ?""")
	#parser.add_argument("-d","--datafile",help="""Quel fichier Fasta souhaite-t-on analyser ?""")
	parser.add_argument("-p","--path_to_file",help="""Chemin vers le fichier à utiliser""")
	return parser.parse_args()

def main():
	args = parse_arguments()
	path_to_file = args.path_to_file
	
	dico_des_sequences = tri.tri(path_to_file)
	
	dico_des_matrices = matHamming.matrices(dico_des_sequences)
	
if __name__ == "__main__": # Sert à executer tout le corp de la fonction main, définie juste au dessus, quand on lance l'execution.
	main()
