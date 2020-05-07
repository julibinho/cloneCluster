#! /usr/bin/env python3
# coding: utf-8
import copy
import networkx as nx
import math
import os
import sys
import numpy as np
import collections as coll

pwd = os.getcwd()
nucleotides = ['a','c','g','t']
q = len(nucleotides)



#lire les seq : 


##################################################################
#                   Lecture des fichiers de Fair (ou autre)
###################################################################
def index(l,elem):
    for i in range(len(l)):
        if l[i].lower() == elem.lower():
            return i
    return -1

def to_string(l_seqs):
    res = " ".join(s for s in l_seqs)
    return res
###########################################
#             Score profile vs profile
###########################################
def dotProd(P1, P2):
    L = np.size(P1,1)
    N = np.size(P1,0)
    s=0
    for j in range(L):
        for i in range(N):
            #print (P1[i][j], P2[i][j])
            s = s + P1[i][j]*P2[i][j]
    return s

def get_Q(P):
	q = len(nucleotides)
	L = np.size(P,1) #nombre de colonnes
	#print(q, L)
	PWM = np.zeros((q, L))
	for i in range(L):
		col_i = P[:,i]
		freq = coll.Counter(col_i) 
		#print(freq)
		for j, a in enumerate(nucleotides): 
			#print(j,a)
			PWM[j][i] = freq[a]
	PWM = PWM + 1            
	return (PWM)/(np.sum(PWM, axis=0))
	
	
	
def distance_profiles(P1, P2):
    #print('nouvelle distance')
    Q1 = get_Q(P1)
    Q2 = get_Q(P2)
    #print('\nP1:', P1,'\tP2:', P2)
    #print('\nQ1:', Q1,'\tQ2:', Q2)
    return dotProd(Q1, Q2)




###########################################
#             Fonction de lecture
###########################################


def sequences_reader(path_to_file): 
	dico = {}
	with open(path_to_file, "r") as fasta_file:
		for line in fasta_file:
			if line.startswith(">"):
				name = line.strip()[1:]
				if not name.startswith('S'):
				    name = 'S' + name
			else:
				seq = line.strip()
				dico[name]=seq
	return dico # S1: 'AACC...

##########################################################
#         Création de profils des clusters
##########################################################

def create_profile(seqs, ref):
    seqs = list(set([ref[s] for s in seqs if s in ref])) 
    prof = []
    if seqs == []:
        return np.array([[]])
    if len(seqs) == 1:
        #print([[i] for i in seqs[0]])
        return np.array([[i for i in seqs[0]]])
    for i in range(len(seqs)):
        temp=[]
        for j in range(len(seqs[i])):
            temp.append(seqs[i][j].lower())
        prof.append(temp)
    #print(prof)
    return np.array(prof)
    
##########################################################
#         Fonctions principales
##########################################################

def reader(path_to_file, path_to_data):  #equivalent de tri_cle_valeur dans graph_input
    ref = sequences_reader(path_to_data)
    #print(ref, '\n\n')
    #print(ref)
    clusters = {}
    with open(path_to_file, "r") as file:
        for line in file:
            clust = line.strip().split()
            seqs = clust[1:]
            profile = create_profile(seqs, ref)
            #print('\n',profile)
            if len(profile) != 0:
                if len(profile[0]) not in clusters:
                    clusters[len(profile[0])]={to_string(seqs) : profile} # On fait comme pour tri_cle_valeur : dico de dico
                else :
                    clusters[len(profile[0])][to_string(seqs)] = profile
    #print(clusters)
    return clusters 
    

def instanciation_des_graphes_cle_valeur(dico): #prends en entrée un dictionnaire avec des sequences
	#print('génération des graphes')
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
			##############
				d = distance_profiles(dico[w][y], seq)
				G_courant.add_edge(x,y)
				G_courant[x][y]['weight'] = d
		res[w] = G_courant
		#print(id, ' arretes de poids inférieur à 0.3w pour la taille ', w, ' parmis ',count , 'arretes' )
	return res #retourne un dictionnaire de graphes

def generate_graphs_consensus(path_to_file,path_to_data):
	return instanciation_des_graphes_cle_valeur(reader(path_to_file,path_to_data))



def main():
    #print(alignement(nucleotides,1,-2,'catgac','tctgaac',-1))
    res = generate_graphs_consensus("/home/lisa/Programmation/cloneCluster/data/Tools_output/IMGT_output/Real_data/I1_IMGT_Fo.txt", "/home/lisa/Programmation/cloneCluster/data/Real/Extracted_CDR3/Extracted_by_IMGT/I1_oligo_CDR3_NA.txt")
    #reader("/home/lisa/Programmation/cloneCluster/data/Tools_output/IMGT_output/Real_data/I1_IMGT_Fo.txt", "/home/lisa/Programmation/cloneCluster/data/Real/Extracted_CDR3/Extracted_by_IMGT/I1_oligo_CDR3_NA.txt")
    #res = create_profile(['A', 'B', 'C'], {'A':'ATG', 'B':'CTT', 'C':'ACT'})
    #print(res)
    #print(get_Q(res))
    
    
if __name__ == "__main__":
    main()
