#! /usr/bin/env python3
# coding: utf-8

import numpy as np

def distance_Hamming(seq1, seq2):
    distance=0
    for i in range (len(seq1)):
        if seq1[i]!=seq2[i]:
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
    
def matrices(dico):
	res = {}
	for w in dico.keys():
		res[w] = matrice_adjacence_Hamming(dico[w])
	return res

def main():
	pass
	
if __name__ == "__main__":
	matrice_adjacence_Hamming(['a','a'])


