#! /usr/bin/env python3
# coding: utf-8
import copy
import networkx as nx
import math
import align_mult
import os
pwd = os.getcwd()
################################################################
#   lit les fichiers résultats de Fair
################################################################
nucleotides = ['a','c','g','t']


##################################################################
#                   Lecture des fichiers de Fair (ou autre)
###################################################################
def index(l,elem):
    for i in range(len(l)):
        if l[i].lower() == elem.lower():
            return i
    return 0

	
def Id_vers_seq(l_seqs,ref):
    res = []
    for s in l_seqs:
        if s in ref:
            res.append(ref[s])
    return res


def seq_consensus(seq):
    res = ''
    for nucl in seq:
        p_max = 0
        position = 0
        #print(nucl)
        for proba in nucl:
            if proba > p_max:
                p_max = proba
                position = nucl.index(proba)
        res += nucleotides[position]
    #print('dans seq_consensus', res)
    return res

def blast_score(X1, X2):
    #print(X1, X2)
    with open(pwd + '/seq1.fa', "w") as fichier1:
        fichier1.write('>S1\n'+seq_consensus(X1))
    with open(pwd + '/seq2.fa', "w") as fichier2:
        fichier2.write('>S2\n'+seq_consensus(X2))
    res = align_mult.dist_blast('seq1.fa', 'seq2.fa' )
    #sprint('res blast_score : ', res)
    return res
    
def distance_euclidienne(X1,X2):
    d = 0
    for i in range(len(X1)):
        d += (X1[i] - X2[i])**2
    return math.sqrt(d)

def distance_seqs(seq1,seq2): #où seq1 et seq2 sont des séquences consensus
    distance=0
    for i in range (len(seq1)):
        distance += distance_euclidienne(seq1[i],seq2[i])
    return(distance)

    
def to_string(l_seqs):
    res = " ".join(s for s in l_seqs)
    return res
    
###########################################
#             Fonction de lecture
###########################################




def sequences_reader(path_to_file): 
	dico = {}
	with open(path_to_file, "r") as fasta_file:
		for line in fasta_file:
			if line.startswith(">"):
				name = line.strip()[1:]
				#name = 'S' + name
			else:
				seq = line.strip()
				dico[name]=seq
	return dico # S1: 'AACC...


########################################################################
#     Permet de décider si on a besoin d'un alignement ou non 
########################################################################

def verif_taille(l_seqs,ref):
    #print(l_seqs)
    #print('dans verif taille')
    i = 0
    while l_seqs[i] not in ref :
        if i< len(l_seqs)-1 :
            i +=1
        else :
            break
    res = True
    if l_seqs[i] in ref:
        cible = len(ref[l_seqs[i]])
        #print(ref[l_seqs[i]])
        for s in l_seqs[1:]:
            if s in ref :
                #print(ref[s])
                if len(ref[s]) != cible:
                    #print('pas la même taille')
                    res = False
    else :
        #print('dans le else')
        return False #Aucunes des séquences du cluster n'est présente dans le dictionnaire
    #print(res)
    return res

####################################################
#       Calcule la séquence consensus
####################################################

    
def cons(l_seqs, ref): #liste des id des séquences du cluster et dictionnaire de référence de toutes les séquences
    if verif_taille(l_seqs,ref):
        l_seqs = Id_vers_seq(l_seqs,ref) #l_seqs contient maintenant les séquences, et plus les ID
        
        N = len(l_seqs) # nombres de séquences
        M = len(l_seqs[0])
        res = [[0,0,0,0] for i in range(M)]
        #print('nouveau cluster : ', l_seqs)
        for seq in l_seqs:
            for i in range(M):
                res[i][index(nucleotides,seq[i])] +=1
            
        for i in range(M):
            for j in range(len(res[i])):
                res[i][j] = res[i][j]/ (N) # on normalise le résultat,
        #print(res)
        return res
    else :
        l_seqs = Id_vers_seq(l_seqs,ref)
        with open(pwd + '/fasta_clust.fa', "w") as fichier:
            #print(' jfdkls', pwd)
            count = 1
            for s in l_seqs:
                fichier.write('>S' + str(count) +'\n' + s + '\n')
                count += 1
        res = align_mult.align_mult('fasta_clust.fa' )
        #print('Attention, les séquences au sein d\'un même cluster n\'ont pas toutes la même taille!')
        #os.system('rm fasta_clust.fa')
        return res

##########################################################
#         Fonctions principales
##########################################################

def reader(path_to_file, path_to_data):  #equivalent de tri_cle_valeur dans graph_input
    ref = sequences_reader(path_to_data)
    #print(ref)
    clusters = {}
    with open(path_to_file, "r") as file:
        for line in file:
            clust = line.strip().split()
            seqs = clust[1:]
            consensus = cons(seqs, ref)
            if len(consensus) != 0:
                if len(consensus) not in clusters:
                    clusters[len(consensus)]={to_string(seqs) : consensus} # On fait comme pour tri_cle_valeur : dico de dico
                else :
                    clusters[len(consensus)][to_string(seqs)] = consensus
    return clusters 
    

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
			    ##############
				d = distance_seqs(dico[w][y], seq)
				#####################
				#d = blast_score(dico[w][y], seq) # ne marche pas
				##########################
				#if d < 0.5 * w :
				#	id +=1
				#count +=1
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
    #print(res)
    
if __name__ == "__main__":
    main()

