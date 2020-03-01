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
# =============================================================================
#         Print a gaphe where the edges are the link in the result file, 
#        and the color of the nodes are the link in the true cluster file 
# =============================================================================	
def print_res(res,tc):

	
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
def readResultFile(filename):
	cluster = {}; count = 0; totalSeq = 0;
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
				totalSeq += len(arraySeqIds)
	file.close()
	#print ("Total clusters = ", count," Total sequences = " , totalSeq)
	return  cluster,totalSeq
	
# =============================================================================
#               Read true cluster file
# =============================================================================	
def readTrueClusterFile(filename):
	hashCluster = {}; count = 0; countCluster = 0;
	hashCluster_detail = {}
	file = open(filename, "r")
	for line in file.readlines(): 
		IDcluster = int(line.split('\t')[0].rstrip())
		seq = line.split('\t')[1].split(" ")
		seq[-1] = seq[-1].rstrip()
		#print seq
		for s in seq:
			#hashCluster_detail[int(s)] = IDcluster
			hashCluster_detail[s] = IDcluster
		hashCluster[int(IDcluster)] = len(seq)
	file.close()
	#print hashCluster,"hashclister"
	return  hashCluster, hashCluster_detail
	
	
# =============================================================================

def main():
	#result,totalSeq = readResultFile('/home/lisa/Programmation/cloneCluster/algoCluster/Louvain/results/res.txt') #result est sous la forme d'un 
	#true_c,totalSeq = readResultFile('/home/lisa/Programmation/cloneCluster/data/artficial/True_clusters/monoclonal_simp_indel_true_clusters.txt')
	#print(true_c)#,totalSeq,true_c,detail)
	result,totalSeq = readResultFile('res_toy.txt')
	true_c,totalSeq = readResultFile('true_toy.txt')
	print_res(result, true_c)
	#print_louvain(part)
	
if __name__ == "__main__":
	main()



