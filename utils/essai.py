#! /usr/bin/env python3
# coding: utf-8

import networkx as nx


def distance_Hamming(seq1, seq2):
    distance=0
    for i in range (len(seq1)):
        if seq1[i]==seq2[i]: ## j'ai modifié la distance de Hamming ici, pour que les séquences identiques soient plus liées entre elles que les séquences différentes
            distance +=1
    return(distance)

def generate_graph(path_to_file):
	dico = {}
	with open(path_to_file, "r") as fasta_file:
		for line in fasta_file:
			if line.startswith(">"):
				name = line.strip()[1:]
			else:
				seq = line.strip()
				n = len(seq)
				if n not in dico :
					dico[n] = nx.Graph()
					dico[n].add_node(name, sequence=seq)
					
					#print(dico[n][name])
					#dico[n][name]['sequence']=seq
					#{name : seq}
				else :
					dico[n].add_node(name, sequence=seq)
					
					for node in list(dico[n].nodes(data=True)): #node est un couple avec comme premier element le nom de la sequence, et en deuxième element un dictionnaire avec l'association 'sequence' et la sequence
						d = distance_Hamming(seq,node[1]['sequence'])
						dico[n].add_edge(name,node[0])
						dico[n][name][node[0]]['weight'] = d
	return dico #rend un dictionnaire avec les longeur des séquences comme clés, et un dictionnaire associant nom et séquences. Finalement, on a un dictionnaire de dictionnaires. s


def main():
	generate_graph('/home/lisa/Programmation/cloneCluster/data/artficial/Extracted_CDR3/monoclonal_simp_indel_cdr3.fa')

if __name__ == "__main__":
	main()
