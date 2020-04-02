import os
import sys
pwd = os.getcwd()
sys.path.append(pwd+'/tool')
import numpy as np
from sklearn.neighbors import kneighbors_graph

X = [[0], [3], [1]]
def initialisation(M):
    S=matrice_adjacence_Hamming(M)
    d=[]
    for i in range (len(S)):
        degree=np.sum(S,axis=0)[i]
        d.append(degree)
    D=np.diag(d)
    return(S,D)
def matrice_adjacence_Hamming(seqs):
    n = len(seqs)
    M=np.zeros((n,n))
    for i in range (n):
        for j in range (i+1 ,n):
                d= distance_Hamming(seqs[i], seqs[j])
                M[i][j] = d
                M[j][i] = d #les matrices sont symétriques
    return(M)

def distance_Hamming(seq1, seq2):
    distance=0
    for i in range (len(seq1)):
        if seq1[i]==seq2[i]: # Objectif : les séquences identiques soient plus liées entre elles que les séquences différentes
            distance +=1
    return(distance)

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
	return dico

def k_nearest(D,n_neig):
    graph=kneighbors_graph(D,n_neig,mode='connectivity', include_self=True)
    return(graph)

def eigen(M):
    vals,vect=np.linalg.eig(M)
    vals=np.real(vals)
    vals=np.sort(vals) #On trie de manière croissante les valeurs propres obtenues
    print(vals)
    vect=np.real(vect)
    vals=np.array(vals)
    vect=np.array(vect)
    return(vals,vect)


dico_seq=tri_cle_valeur('C:\\Users\\quent\\ProjetBIM\\cloneCluster\\data\\Artificial\\Extracted_CDR3\\monoclonal_simp_indel_cdr3.fa')
print("dico_seq",dico_seq)
sequences=[]
for p in dico_seq[50].keys():
    sequences.append(dico_seq[50][p])
sequences =np.array(sequences)
nb_sequences=len(sequences)
Adj,Diag=initialisation(sequences)
k_neig_graph=k_nearest(Adj,5)
matrix=k_neig_graph.toarray()
print(matrix)
print("Adj",Adj)