#! /usr/bin/env python3
# coding: utf-8

import numpy as np
import networkx as nx
import pandas as pd
import copy

def distance_Hamming(seq1, seq2):
    distance=0
    for i in range (len(seq1)):
        if seq1[i]==seq2[i]: ## j'ai modifié la distance de Hamming ici, pour que les séquences identiques soient plus liées entre elles que les séquences différentes
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
		#if w == 44 :
		        #print "dans matrices, avec : ", res[w]
	return res
	
	



	
def instanciation_des_graphes_cle_valeur(dico): #prends en entrée un dictionnaire avec des graphes comme valeurs
	res = {}
	d2 = copy.deepcopy(dico) #copie indépendante de l'entrée
	for w in dico.keys():
		#print(w, ' : ', dico[w], '\n\n\n')
		G_courant = nx.Graph()
		for x in dico[w].keys():
			seq = d2[w].pop(x) # on retire la séquences courante du dictionnaire d2, qui mémorise les séquences déjà parcourues
			for y in d2[w].keys() : #on ne calcule la distance que pour les séquences qui n'ont pas encore étées parcourues. 
				d = distance_Hamming(dico[w][y], seq)
				G_courant.add_edge(x,y)
				G_courant[x][y]['weight'] = d
		res[w] = G_courant
	return res #retourne un dictionnaire de graphes

def main():
	matrice_adjacence_Hamming(['a','a'])
	
if __name__ == "__main__":
	main()


