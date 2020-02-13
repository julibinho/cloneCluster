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

#import pylab as P
def cluster_louvain(dico):
	res = {}
	for w in dico.keys():
		res[w] = cmty.best_partition(dico[w])
	return res


def print_louvain(partition):
	#drawing
	print partition
	G = nx.Graph()
	lab = {}
	for y in partition.keys():
		G.add_node(y)
		lab[y]=y
	#affichage.affiche_G_avec_poids(G)
	size = float(len(set(partition.values())))
	for com in set(partition.values()) :
		list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
		for x in list_nodes :
			for y in list_nodes :
				if x != y :
					G.add_edge(x,y)
	pos = nx.spring_layout(G)
	count = 0.
	for com in set(partition.values()) :
		count = count + 1.
		list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
		for x in list_nodes :
			for y in list_nodes :
				if x != y :
					G.add_edge(x,y)
		nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20, node_color = str(count / size))
	nx.draw_networkx_labels(G,pos,labels = lab,font_size=12)

	nx.draw_networkx_edges(G, pos, alpha=0.5)
	plt.show()


def main():
	pass
	


	
if __name__ == "__main__":
	main()



