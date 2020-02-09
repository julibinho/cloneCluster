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
	#print lab
	nx.draw(G)
	edge_labels=nx.draw_networkx_edge_labels(G,pos=nx.spring_layout(G), edge_labels=lab, label_pos=0.5, font_size=10, font_color='k', font_family='sans-serif', font_weight='normal', alpha=1.0, bbox=None, ax=None, rotate=True)
	plt.show()
	

