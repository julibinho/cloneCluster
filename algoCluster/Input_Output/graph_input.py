#! /usr/bin/env python3
# coding: utf-8

import networkx as nx
import copy
import numpy as  np

################################################################
#   génère les graphes networkx pour l'utilisation de Louvain
################################################################

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
	#print('tri clé-valeurs OK')
	return dico #rend un dictionnaire avec les longeur des séquences comme clés, et un dictionnaire associant nom et séquences. Finalement, on a un dictionnaire de dictionnaires. 

def distance_Hamming(seq1, seq2):
    distance=0
    for i in range (len(seq1)):
        if seq1[i]==seq2[i]: # Objectif : les séquences identiques soient plus liées entre elles que les séquences différentes
            distance +=1
    distance = distance/ len(seq1)
    return(distance)


def instanciation_des_graphes_cle_valeur(dico): #prends en entrée un dictionnaire avec des sequences
	res = {}
	#count = 0
	#id = 0
	d2 = copy.deepcopy(dico) #copie indépendante de l'entrée
	for w in dico.keys():
		G_courant = nx.Graph()
		for x in dico[w].keys():
			seq = d2[w].pop(x) # on retire la séquences courante du dictionnaire d2, qui mémorise les séquences déjà parcourues
			G_courant.add_node(x) #certaines séquences sont les seules de leur taille
			for y in d2[w].keys() : #on ne calcule la distance que pour les séquences qui n'ont pas encore étées parcourues. 
				d = distance_Hamming(dico[w][y], seq)
				#if d < 0.5 * w :
				#	id +=1
				#count +=1
				G_courant.add_edge(x,y)
				G_courant[x][y]['weight'] = d
		res[w] = G_courant
		#print(id, ' arretes de poids inférieur à 0.3w pour la taille ', w, ' parmis ',count , 'arretes' )
	return res #retourne un dictionnaire de graphes


def generate_graphs(path_to_file):
	return instanciation_des_graphes_cle_valeur(tri_cle_valeur(path_to_file))
	
	
###############################################	
# génère les matrices de distances 
###############################################


def matrix(dico):
    n = len(dico)
    M=np.zeros((n,n))
    seqs = list(dico.keys())
    for i in range (n):
        for j in range (i+1 ,n):
                d= distance_Hamming(dico[seqs[i]], dico[seqs[j]])
                M[i][j] = d
                M[j][i] = d #les matrices sont symétriques
    return(M)
    

	
def generate_matrix(path_to_file):
	dico = tri_cle_valeur(path_to_file)
	res = {}
	for w in dico.keys():
		res[w] = matrix(dico[w])
	return res
		
	
	
	
	
	
	
#####################################################################################
#   génère le dictionnaire des graphes, ainsi que un dictionnaire d'initialisation,
#           qui précise dans quel cluster sont les séquences au début. 
#      On choisi de mettre dans le même cluster les séquences identiques
#####################################################################################
	
	
def generate_graphs_and_init(path): #prends en entrée un dictionnaire avec des sequences
	dico = tri_cle_valeur(path)
	res = {}
	init = {}
	d2 = copy.deepcopy(dico) #copie indépendante de l'entrée
	#print(dico)
	for w in dico.keys():
	
		count = 0
		init_courant= {}
		G_courant = nx.Graph()
		for x in dico[w].keys():
			seq = d2[w].pop(x) # on retire la séquences courante du dictionnaire d2, qui mémorise les séquences déjà parcourues
			G_courant.add_node(x) #certaines séquences sont les seules de leur taille
			for y in d2[w].keys() : #on ne calcule la distance que pour les séquences qui n'ont pas encore étées parcourues. 
				d = distance_Hamming(dico[w][y], seq)
				G_courant.add_edge(x,y)
				G_courant[x][y]['weight'] = d
				if d == w: # la séquence est identique à l'une des séquences déjà parcourues
					if x not in init_courant:
						init_courant[x] = count
						init_courant[y] = count
						count += 1
					elif y not in init_courant :
						init_courant[y] = init_courant[x] 
			if x not in init_courant:
				init_courant[x] = count
				count +=1
		res[w] = G_courant
		init[w] = init_courant
	return res, init #retourne un dictionnaire de graphes


	
