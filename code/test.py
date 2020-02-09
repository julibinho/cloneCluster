#! /usr/bin/env python3
# coding: utf-8

import community as cmty
from networkx import *
import networkx as nx
import matplotlib.pyplot as plt
import tri_des_seq as tri
import matrice_distance_hamming as hamming
import affichage
import numpy as np
import pandas as pd

dict = {'S731': 'gtgcgatggaagctgactaccagctagcctactttgactactgg',
'S40': 'gtgcgagagacgaggtggtggagtactacggtatggacgtctgg',
'S678': 'gtgcgagagacgaggtggtggagtactacggtatggacgtctgg',
'S679': 'gtgcgagagacgaggtggtggagtactacggtatggacgtctgg',
'S673': 'gtgcgagagacgaggtggtggagtactacggtatggacgtctgg',
'S676': 'gtgcgagagacgaggtggtggagtactacggtatggacgtctgg',
'S677': 'gtgcgagagacgaggtggtggagtactacggtatggacgtctgg',
'S675': 'gtgcgagagacgaggtggtggagtactacggtatggacgtctgg',
'S580': 'gtgcaagaagaggtataaccggaaccaactggttcgactcctgg',
'S581': 'gtgcaagaagaggtataaccggaaccaactggttcgactcctgg',
'S430': 'gtgcgagagacgaggtggtggagtactacggtatggacgtctgg',
'S302': 'gtgcgatggaagctgactaccagctagcctactttgactactgg',
'S426': 'gtgcgagagacgaggtggtggagtactacggtatggacgtctgg',
'S809': 'gtgcgatggaagctgactaccagctagcctactttgactactgg',
'S282': 'gtgtgaacaaaggtatttttggacacgtcgacttccagcactgg',
'S836': 'gtgcgatggaagctgactaccagctagcctactttgactactgg',
'S394': 'gtgcaagaagaggtataaccggaaccaactggttcgactcctgg',
'S578': 'gtgcaagaagaggtataaccggaaccaactggttcgactcctgg',
'S577': 'gtgcaagaagaggtataaccggaaccaactggttcgactcctgg',
'S441': 'gtgtgaacaaaggtatttttggacacgtcgacttccagcactgg',
'S680': 'gtgcgagagacgaggtggtggagtactacggtatggacgtctgg',
'S552': 'gtgcaagaagaggtataaccggaaccaactggttcgactcctgg',
'S438': 'gtgtgaacaaaggtatttttggacacgtcgacttccagcactgg',
'S439': 'gtgtgaacaaaggtatttttggacacgtcgacttccagcactgg',
'S437': 'gtgtgaacaaaggtacttttggacacgtcgacttccagcactgg'}


D = {44 : dict}

def distance_Hamming(seq1, seq2):
    distance=0
    for i in range (len(seq1)):
        if seq1[i]==seq2[i]: ## j'ai modifié la distance de Hamming ici, pour que les séquences identiques soient plus liées entre elles que les séquences différentes
            distance +=1
    return(distance)

def instanciation_des_graphes_cle_valeur(dico): #prends en entrée un dictionnaire avec des graphes comme valeurs
	res = {}
	for w in dico.keys():
		print 'w : ', w
		G_courant = nx.Graph()
		for x in dico[w].keys():
			seq = dico[w].pop(x)
			for y in dico[w].keys() :
				d = distance_Hamming(dico[w][y], seq)
				G_courant.add_edge(x,y)
				G_courant[x][y]['weight'] = d
		res[w] = G_courant
	return res
					
dic_des_G = instanciation_des_graphes(D)
affichage.affiche_G_avec_poids(dic_des_G[44])


def print_louvain(G):
	partition = cmty.best_partition(G)

	#drawing
	size = float(len(set(partition.values())))
	pos = nx.spring_layout(G)
	count = 0.
	for com in set(partition.values()) :
		count = count + 1.
		list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
		nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20, node_color = str(count / size))


	nx.draw_networkx_edges(G, pos, alpha=0.5)
	plt.show()
	#print partition
	return partition

print print_louvain(dic_des_G[44])

