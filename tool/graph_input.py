#! /usr/bin/env python3
# coding: utf-8

import networkx as nx
import copy


def tri_cle_valeur(path_to_file):
	dico = {}
	with open(path_to_file, "r") as fasta_file:
		for line in fasta_file:
			if line.startswith(">"):
				name = line.strip()[1:]
			else:
				seq = line.strip()
				if len(seq) not in dico :
					dico[len(seq)] = {name : seq}
				else :
					dico[len(seq)][name] = seq
	return dico #rend un dictionnaire avec les longeur des séquences comme clés, et un dictionnaire associant nom et séquences. Finalement, on a un dictionnaire de dictionnaires. 

def distance_Hamming(seq1, seq2):
    distance=0
    for i in range (len(seq1)):
        if seq1[i]==seq2[i]: # Objectif : les séquences identiques soient plus liées entre elles que les séquences différentes
            distance +=1
    return(distance)


def instanciation_des_graphes_cle_valeur(dico): #prends en entrée un dictionnaire avec des graphes comme valeurs
	res = {}
	d2 = copy.deepcopy(dico) #copie indépendante de l'entrée
	for w in dico.keys():
		G_courant = nx.Graph()
		for x in dico[w].keys():
			seq = d2[w].pop(x) # on retire la séquences courante du dictionnaire d2, qui mémorise les séquences déjà parcourues
			G_courant.add_node(x) #certaines séquences sont les seules de leur taille
			for y in d2[w].keys() : #on ne calcule la distance que pour les séquences qui n'ont pas encore étées parcourues. 
				d = distance_Hamming(dico[w][y], seq)
				G_courant.add_edge(x,y)
				G_courant[x][y]['weight'] = d
		res[w] = G_courant
	return res #retourne un dictionnaire de graphes




def generate_graphs(path_to_file):
	return instanciation_des_graphes_cle_valeur(tri_cle_valeur(path_to_file))
