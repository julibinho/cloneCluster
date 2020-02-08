#! /usr/bin/env python3
# coding: utf-8

import numpy as np
import networkx as nx
import pandas as pd

def distance_Hamming(seq1, seq2):
    distance=0
    for i in range (len(seq1)):
        if seq1[i]==seq2[i]: ## j'ai modifié la distance de Hamming ici, pour que les séquences identiques soient plus liées entre elles que les séquences différentes
            distance +=1
    return(distance)


def distance_Hamming_panda(seq1, seq2):
    distance=0
    for i in range (len(seq1[1])):
        if seq1[1][i]==seq2[1][i]: ## j'ai modifié la distance de Hamming ici, pour que les séquences identiques soient plus liées entre elles que les séquences différentes
            distance +=1
    return(distance)

def matrice_adjacence_Hamming(seqs):
    n = len(seqs)
    M=np.zeros((n,n))
    for i in range (n):
        for j in range (i+1 ,n):
                d= distance_Hamming(seqs[i], seqs[j])
                M[i][j] = d
                M[j][i] = d #les matrices sont symétriques
    return(M)
    
def matrice_adjacence_Hamming_Panda(seqs):
    n = len(seqs)
    M=np.zeros((n,n))
    for i in range (n):
        for j in range (i+1 ,n):
                d= distance_Hamming_panda(seqs[i], seqs[j])
                M[i][j] = d
                M[j][i] = d #les matrices sont symétriques
    return(M)
    
def matrices(dico):
	res = {}
	for w in dico.keys():
		res[w] = matrice_adjacence_Hamming(dico[w])
		#if w == 44 :
		        #print "dans matrices, avec : ", res[w]
	return res
	
	
def matrices_pandas(dico):
        res = {}
	for w in dico.keys():
		M = matrice_adjacence_Hamming_Panda(dico[w])
		#if w == 44 :
		        #print "dans panda, avec : ",  M, "et avec : ", dico[w]
		names = []
		for i in dico[w] :
		        names.append(i[0])
		Mbis = pd.DataFrame(M,index = names, columns = names)
		#print(Mbis)
		res[w] = Mbis 
	return res
                
                

def instanciation_des_graphes(dico): #prends en entrée un dictionnaire avec des graphes comme valeurs
	res = {}
	for w in dico.keys():
		l = list(dico[w].nodes)
		n = len(l)
		for i in range(n):
			for j in range(i+1,n):
				d = distance_Hamming(l[i][1], l[j][1])
				#print " d :      " , l[i][0],l[j][0],d
				if w not in res:
				        res[w] = nx.Graph()
				        res[w].add_edge((l[i][0],l[j][0]),d)
				else :
				        res[w].add_edge((l[i][0],l[j][0]), d)
				#dico[w].add_edge(l[i],l[j], d) ## Attention, ici les arretes sont mal lues par add, car les l[i] et l[j] sont des tuples, qu'il essaye de séparer...
				#possibilité de générer un networkx à partir d'une matrice panda...
				#dico[w].add_edge(l[i], l[j],{'weight': d} )
				#for k in range(d):
				#dico[w].add_edge(l[i], l[j])
	return res
	


def main():
	matrice_adjacence_Hamming(['a','a'])
	
if __name__ == "__main__":
	main()


