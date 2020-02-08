# -*- coding: utf-8 -*-
from networkx import *
import networkx as nx
#import os
import matplotlib.pyplot as plt
def tri(path_to_file):
	dico = {}
	with open(path_to_file, "r") as fasta_file:
		for line in fasta_file:
			if not line.startswith(">"):
				s = line.strip()
				#Set.append()
				if len(s) not in dico :
					dico[len(s)] = [s]
				else :
					dico[len(s)].append(s)
	#print(dico)
	return dico #rend un dictionnaire avec les longeur des séquences comme clés, et les listes de toutes les sequences de cette longueur comme valeur. 
def tri_pandas(path_to_file):	 #l'idée c'était de transformer une matrice panda en networkx, mais il faut un formalisme spécial pour la forme des matrices : il faut que chaque ligne représente un arc, et ce n'est pas le cas dans ce qui est fait ici. Il faudra reprendre, ou trouver un autre moyens d'avoir le bon graphe. 
	dico = {}
	with open(path_to_file, "r") as fasta_file:
		for line in fasta_file:
			if line.startswith(">"):
				name = line.strip()[1:]
			else :
				seq = line.strip()
				if len(seq) not in dico :
					dico[len(seq)] = [(name,seq)]
				else :
					dico[len(seq)].append((name,seq))
	#print(dico)
	return dico #rend un dictionnaire avec les longeur des séquences comme clés, et les listes de toutes les sequences de cette longueur comme valeur. 
	
	
	
def creation_des_graphes(path_to_file):
	dico = {}
	with open(path_to_file, "r") as fasta_file:
		for line in fasta_file:
			if line.startswith(">"):
				name = line.strip()[1:]
			else :
				seq = line.strip()
				if len(seq) not in dico :
					dico[len(seq)] = nx.Graph()
					dico[len(seq)].add_node((name,seq))
				else :
					dico[len(seq)].add_node((name,seq))
	#print("done")
	return dico #rend un dictionnaire donc les longueurs sont les clés, et les valeurs sont des networkx avec les noeuds sous la forme (id, séquence)


def main():
	#tri('data/artficial/Extracted_CDR3/monoclonal_simp_indel_cdr3.fa')
	creation_des_graphes('data/artficial/Extracted_CDR3/monoclonal_simp_indel_cdr3.fa')
	
if __name__ == "__main__":
	main()
	
	
	

