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


def main():
	G = nx.erdos_renyi_graph(30, 0.05)
	dico = hamming.instanciation_des_graphes(tri.creation_des_graphes('data/artficial/Extracted_CDR3/monoclonal_simp_indel_cdr3.fa'))
	#for w in dico.keys():
	#	print(w)
		#partition = cmty.best_partition(dico[w],weight='weight')
		
		#
		#print partition 
	#	print_louvain(dico[w])
		#affichage.affiche_G_avec_poids(print_louvain(G))
		#print(type(dico[w]))
		
		#affichage.affiche_G_avec_poids(print_louvain(dico[w]))
	#print(list(dico[15].nodes))
	#print(list(dico[15].edges))
	dicoM = hamming.matrices(tri.tri('data/artficial/Extracted_CDR3/monoclonal_simp_indel_cdr3.fa'))
	dicoPanda = hamming.matrices_pandas(tri.tri_pandas('data/artficial/Extracted_CDR3/monoclonal_simp_indel_cdr3.fa'))
	print dicoM[44],"\n\n\n\n\n\n",  dicoPanda[44]
	#M15 = pd.DataFrame(dicoM[15],index = list('ABCDEFG'), columns = list('ABCDEFG'))
	#affichage.affiche_G_avec_poids(dico[15])
	


	
if __name__ == "__main__":
	main()



