# -*- coding: utf-8 -*-
from networkx import *
import networkx as nx
import matplotlib.pyplot as plt


# =============================================================================
#         Print a gaphe where the edges are the link in the result file, 
#        and the color of the nodes are the link in the true cluster file 
# =============================================================================	
def print_res(file_res,file_tc):

	res = readFile(file_res)
	tc = readFile(file_tc)
	G = nx.Graph()
	lab = {}
	edge = []
	for k in tc.keys():
		for y in tc[k]:
			G.add_node(y) # on ajoute tous les noeuds de true cluster dans le graphe. 
			lab[y]=y
			
	for k in res.keys():
		for i in range(len(res[k])):
			for j in range(i+1, len(res[k])):
				edge.append((res[k][i],res[k][j])) # on ajoute des arretes entre chaque paire de séquences qui appartienne au même cluster
	#print(edge)
	G.add_edges_from(edge)
				
	pos = nx.spring_layout(G)
	count = 0.
	size = len(tc)
	for k in tc.keys():
		count = count + 1.
		nx.draw_networkx_nodes(G, pos, tc[k], node_size = 200, node_color = str(count / (size+1)))
	nx.draw_networkx_edges(G, pos, alpha=0.5)
	plt.show()
	
	
# =============================================================================
#               Read cluster result formatted file
# =============================================================================	
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
	#res_file = '/home/lisa/Programmation/cloneCluster/algoCluster/Louvain/results/res.txt'
	#true_c_file = '/home/lisa/Programmation/cloneCluster/data/artficial/True_clusters/monoclonal_simp_indel_true_clusters.txt'
	
	res_file = 'Archives/res_toy.txt'
	true_c_file = 'Archives/true_toy.txt'
	print_res(res_file, true_c_file)
	
if __name__ == "__main__":
	main()



