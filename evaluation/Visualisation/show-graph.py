# -*- coding: utf-8 -*-
from networkx import *
import networkx as nx
import matplotlib.pyplot as plt
import random
import argparse


# =============================================================================
#         Print a gaphe where the edges are the link in the result file, 
#        and the color of the nodes are the link in the true cluster file 
# =============================================================================	
def print_res(file_res,file_tc):
	
	res = readFile(file_res)
	tc = readFile(file_tc)
	N = len(tc)
	col = random_color(N)
	G = nx.Graph()
	lab = {}
	edge = []
	for k in tc.keys():
		for y in tc[k]:
			G.add_node(y) # on ajoute tous les noeuds de true cluster dans le graphe. 
			lab[y]=y
			
	for k in res.keys():
		for i in range(1,len(res[k])):
			edge.append((res[k][0], res[k][i])) # améliore l'affiche du graphe, les points sont moins centrés sur eux mêmes
	G.add_edges_from(edge)
				
	pos = nx.spring_layout(G)
	ind = 0
	size = len(tc)
	for k in tc.keys():
		nx.draw_networkx_nodes(G, pos, tc[k], node_size = 200, node_color =  col[ind])
		ind +=1
	nx.draw_networkx_edges(G, pos,edge_color = 'grey', alpha=0.5)
	plt.suptitle('the colors of the dots show their cluster in the true_cluster file')
	plt.show()
	
	
# =============================================================================
#                              Usefull
# =============================================================================	
def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-t","--true_cluster",help="""Chemin vers le fichier true cluster""")
	parser.add_argument("-r","--result",help="""Chemin vers le résultat de l'algo""")
	return parser.parse_args()

def random_color(N):
	res = []
	while len(res) != N:
		rand = random.randint(0,16777000) #pour avoir tout le specter de couleurs, il faut aller jusqu'a 16777215, qui se traduit par ffffff et qui est blanc. on veut éviter d'avoir des noeuds blanc, donc le randint ne va que jusqu'
		hex_number = format(rand,'x')
		if len(hex_number) == 6 :
			hex_number = '#' + hex_number
			res.append(hex_number)
	return res

def readFile(filename):
	cluster = {}; count = 0;
	file = open(filename, "r")
	for line in file.readlines(): 
		a=line.split('\t')
		count +=1
		if (count % 5000 == 0): print ("Processed ", count)
		IDcluster = int(a[0])
		members = a[1]

		#print len(members),"members"
		if (members == "\n" or members == ""):
			print ("Warnning:: Cluster ", IDcluster, " has no members")
		else: 
			#delet /n at the end of each line
			arraySeqIds = members.split()
			if arraySeqIds[-1] == '\n':
				arraySeqIds = members.split(" ")[:-1]
			if len(arraySeqIds) != 0:
				cluster[IDcluster] = arraySeqIds
	file.close()
	return  cluster

	
	
# =============================================================================

def main():
	args = parse_arguments()
	path_to_true_cluster = args.true_cluster
	path_to_result = args.result
	
	print_res(path_to_result, path_to_true_cluster)
	
if __name__ == "__main__":
	main()



