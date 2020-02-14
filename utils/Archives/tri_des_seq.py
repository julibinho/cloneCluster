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

def tri_cle_valeur(path_to_file):
	dico = {}
	count = 0
	with open(path_to_file, "r") as fasta_file:
		for line in fasta_file:
			if line.startswith(">"):
				count += 1
				name = line.strip()[1:]
			else:
				seq = line.strip()
				if len(seq) not in dico :
					dico[len(seq)] = {name : seq}
				else :
					dico[len(seq)][name] = seq
	#print(dico)
	countbis = 0
	for w in dico.keys():
		countbis += len(dico[w])
	#print('dans tri : ' , count == countbis, count)
	return dico #rend un dictionnaire avec les longeur des séquences comme clés, et un dictionnaire associant nom et séquences. Finalement, on a un dictionnaire de dictionnaires. 
	
	


def main():
	#tri('data/artficial/Extracted_CDR3/monoclonal_simp_indel_cdr3.fa')
	creation_des_graphes('data/artficial/Extracted_CDR3/monoclonal_simp_indel_cdr3.fa')
	
if __name__ == "__main__":
	main()
	
	
	

