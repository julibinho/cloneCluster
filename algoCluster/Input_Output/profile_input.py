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
            s = s + P1[i][j]*P2[i][j]
    return s

def get_Q(P):
	q = len(nucleotides)
	L = np.size(P,1) #nombre de colonnes
	PWM = np.zeros((q, L))
	for i in range(L):
		col_i = P[:,i]
		freq = coll.Counter(col_i) 
		for j, a in enumerate(nucleotides): 
			if a in freq:
				PWM[j][i] = freq[a]
			elif a.upper() in freq:
				PWM[j][i] = freq[a.upper()]
			else:
				PWM[j][i] = freq[a.lower()]
	PWM = PWM + 1 
	return (PWM)/(np.sum(PWM, axis=0))
	
def wa(Q, p):
    L = np.size(Q,1)
    N = np.size(Q,0)
    W = np.zeros((N, L))
    s=0
    for j in range(L):
        for i in range(N):
            W[i][j] = np.log(Q[i][j]/p[i])
    return W

def p_calcule(PWM):
	return [(sum(PWM[i,:])/np.size(PWM,1)) for i in range(len(nucleotides))]
	
def distance_profiles10(P1, P2): # formule 10
    Q1 = get_Q(P1)
    Q2 = get_Q(P2)
    return dotProd(Q1, Q2)

def distance_profiles11_part(P1, P2): # formule 11
    Q1 = get_Q(P1)
    Q2 = get_Q(P2)
    #print(Q1)
    #print(Q2)
    p1 = p_calcule(Q1)
    p2 = p_calcule(Q2)
    #print('p1,p2', p1,p2)
    W1 = wa(Q1,p1)
    W2 = wa(Q2,p2)
    return dotProd(W1, W2)
    
def distance_profiles11(P1, P2, p): # formule 11
    Q1 = get_Q(P1)
    Q2 = get_Q(P2)
    #print(Q1)
    #print(Q2)
    W1 = wa(Q1,p)
    W2 = wa(Q2,p)
    return dotProd(W1, W2)
def normalize(m, M, s): #normalise le score s selon le m : minimum et M : Maximum
        return (s -m)/(M -m)

def p_generalR(ref):
    count = [1]*q
    tot=q
    for s in ref.values():
        for a in s:
            count[index(nucleotides,a)]+=1
            tot +=1
    for i in range(len(count)):
        count[i] = count[i]/tot
    return count
    
def p_generalD(dico):
    count = [1]*q
    tot=q
    for w in dico.keys():
        for p in dico[w].values():
            for s in p:
                for a in s:
                    count[index(nucleotides,a)]+=1
                    tot +=1
    for i in range(len(count)):
        count[i] = count[i]/tot
    return count

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
    #seqs = list(set([ref[s] for s in seqs if s in ref]))
    seqs = list([ref[s] for s in seqs if s in ref])
    prof = []
    if seqs == []:
        return np.array([[]])
    if len(seqs) == 1:
        return np.array([[i for i in seqs[0]]])
    for i in range(len(seqs)):
        temp=[]
        for j in range(len(seqs[i])):
            temp.append(seqs[i][j].lower())
        prof.append(temp)
    return np.array(prof)
    
##########################################################
#         Fonctions principales
##########################################################

def reader(path_to_file, path_to_data):  #equivalent de tri_cle_valeur dans graph_input
    ref = sequences_reader(path_to_data)
    clusters = {}
    with open(path_to_file, "r") as file:
        for line in file:
            clust = line.strip().split()
            seqs = clust[1:]
            profile = create_profile(seqs, ref)
            if len(profile) != 0:
                if len(profile[0]) not in clusters:
                    clusters[len(profile[0])]={to_string(seqs) : profile} # On fait comme pour tri_cle_valeur : dico de dico
                else :
                    clusters[len(profile[0])][to_string(seqs)] = profile
    return clusters 
    

def instanciation_des_graphes_cle_valeur(dico): #prends en entrée un dictionnaire avec des profiles
	res = {}
	p = p_generalD(dico)
	count = 0
	count_tot = 0
	d2 = copy.deepcopy(dico) #copie indépendante de l'entrée
	for w in dico.keys():
		G_courant = nx.Graph()
		m = math.inf
		M = -math.inf
		for x in dico[w].keys():
			seq = d2[w][x]
			G_courant.add_node(x) 
			for y in d2[w].keys() : 
				d = distance_profiles11(dico[w][y], seq,p)
				if d > M:
					M = d
				if d < m:
					m = d
		for x in dico[w].keys():
			seq = d2[w].pop(x) # on retire la séquences courante du dictionnaire d2, qui mémorise les séquences déjà parcourues
			G_courant.add_node(x) #certaines séquences sont les seules de leur taille
			for y in d2[w].keys() : #on ne calcule la distance que pour les séquences qui n'ont pas encore étées parcourues. 
			##############
				d = distance_profiles11(dico[w][y], seq,p)
				#print(d)
				d= normalize(m,M,d)
				#print(d)
				count_tot +=1
				if d >=0:
					G_courant.add_edge(x,y)
					G_courant[x][y]['weight'] = d
				else :
					count+=1
		res[w] = G_courant
	#print('\n\n', count_tot, count)
	return res #retourne un dictionnaire de graphes

def generate_graphs_consensus(path_to_file,path_to_data):
	return instanciation_des_graphes_cle_valeur(reader(path_to_file,path_to_data))



def main():
    #print(alignement(nucleotides,1,-2,'catgac','tctgaac',-1))
    #res = generate_graphs_consensus("/home/lisa/Programmation/cloneCluster/data/Tools_output/IMGT_output/Real_data/I1_IMGT_Fo.txt", "/home/lisa/Programmation/cloneCluster/data/Real/Extracted_CDR3/Extracted_by_IMGT/I1_oligo_CDR3_NA.txt")
    #reader("/home/lisa/Programmation/cloneCluster/data/Tools_output/IMGT_output/Real_data/I1_IMGT_Fo.txt", "/home/lisa/Programmation/cloneCluster/data/Real/Extracted_CDR3/Extracted_by_IMGT/I1_oligo_CDR3_NA.txt")
    #res = create_profile(['A', 'B', 'C'], {'A':'ATG', 'B':'CTT', 'C':'ACT'})
    #print(res)
    #print(get_Q(res))
    #P1 = np.array([['A', 'T', 'G'], ['C',  'T', 'T'], ['A',  'C', 'T']])
    #P2 = np.array([['T', 'G', 'C'], ['T',  'A', 'C'], ['C',  'G', 'C']])
    #P2 = np.array([['T', 'G', 'C'], ['T',  'G', 'C'], ['G',  'A', 'A']])
    #print('dist', distance_profiles10(P1,P1))
    #print(distance_profiles10(P1,P2))
    #print(distance_profiles11(P1,P1))
    #print(distance_profiles11(P1,P2))
    P1 = np.array([['A', 'T', 'G'], ['A',  'T', 'G'], ['A',  'T', 'G'], ['A',  'T', 'G']])
    #P1 = np.array([['A', 'T', 'G'], ['C',  'C', 'C'], ['A',  'A', 'A']])
    #P2 = np.array([['T', 'G', 'C'], ['T',  'A', 'C'], ['C',  'G', 'C']])
    P2 = np.array([['T', 'A', 'T'], ['T',  'A', 'T'], ['T',  'A', 'T'], ['T',  'A', 'T']])   
    P3 = np.array([['T', 'T', 'T'], ['T',  'T', 'T'], ['T',  'T', 'T'], ['T',  'T', 'T']]) 
    ref = {1:'ATG', 2: 'ATG',3:'ATG',4:'ATG',5:'TAT',6:'TAT',7:'TAT',8:'TAT', 9:'TTT',10:'TTT',11:'TTT',12:'TTT'}
    print(p_generalR(ref))
    print(p_generalD({3:{1: P1, 2:P2, 3:P3}}))
    
    p = p_generalD({3:{1: P1, 2:P2, 3:P3}})
    print('part', distance_profiles11_part(P1,P1))
    print('norm', distance_profiles11(P1,P1, p))
    print(distance_profiles11(P2,P2, p))
    print(distance_profiles11(P3,P3, p))
    print(distance_profiles11(P1,P2, p))
    print(distance_profiles11(P1,P3, p))
    print(distance_profiles11(P3,P2, p))
    
if __name__ == "__main__":
    main()
