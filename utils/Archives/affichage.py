# -*- coding: utf-8 -*-
from networkx import *
import networkx as nx
import matplotlib.pyplot as plt

def affiche_G_avec_poids(G):
	lab = {}
	for i in list(G.edges(data=True)) :
		#print i
		if len(i) == 3 :
			lab[(i[0],i[1])] = '%d' % i[2]['weight']
			#print i[2]
	#print lab
	nx.draw(G)
	edge_labels=nx.draw_networkx_edge_labels(G,pos=nx.spring_layout(G), edge_labels=lab, label_pos=0.5, font_size=10, font_color='k', font_family='sans-serif', font_weight='normal', alpha=1.0, bbox=None, ax=None, rotate=True)
	plt.show()
	


def print_louvain(partition):
	#drawing
	print(partition)
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





def print_louvain(partition):
	#drawing
	print(partition)
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

