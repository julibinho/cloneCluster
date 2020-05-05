#! /usr/bin/env python3
# coding: utf-8
import os
pwd = os.getcwd()
import networkx as nx
import subprocess
import copy
nucl = ['A','C','G','T']
def index(l, elem):
    for i in range(len(l)):
        if l[i].upper() == elem.upper():
            return i

def to_string(l_seqs):
    res = " ".join(s for s in l_seqs)
    return res
    
    
    
def cons(seqs, ref):
    #print('\n\n')
    seqs = list(set([ref[s] for s in seqs if s in ref]))
    #print(seqs)
    if len(seqs) == 1:
        return seqs[0]
    elif len(seqs) == 0: #aucune des séquences du cluster n'est référencées 
        return ''
    with open(pwd + '/fasta_clust.fa', "w") as fichier:
        count = 1
        for s in seqs:
            #print(s)
            fichier.write('>S' + str(count) +'\n' + s + '\n')
            count += 1
    subprocess.run(["edialign",  "fasta_clust.fa",  "out.txt", "align.fa"], capture_output = True)
    subprocess.run(['em_cons', 'align.fa', 'cons.fa'], capture_output = True)
    with open(pwd + '/cons.fa', 'r') as fasta:
        res = ''
        for line in fasta:
            if not line.startswith('>'):
                res = res + line.strip()
    os.system('rm fasta_clust.fa out.txt align.fa cons.fa')
    return res
    
    
    
def cons_bis(seqs,ref):
    seqs = list(set([ref[s] for s in seqs if s in ref]))
    seq_cons = ''
    if len(seqs) == 1:
        return seqs[0]
    elif len(seqs) == 0:
        return seq_cons
    for i in range(len(seqs[0])): # on parcours toutes les position pour trouver le nucléotide majoritaire
        compt = [0]*len(nucl)
        for j in range(len(seqs)):
            compt[index(nucl,seqs[j][i])] +=1
        nucl_max = 0
        score_max = 0
        for i in range(len(compt)):
            if compt[i] > score_max:
                score_max = compt[i]
                nucl_max = i
        if compt.index(score_max) == nucl_max: # le score max n'apparait qu'un fois
            seq_cons = seq_cons + nucl[nucl_max]
        else :
            choix = []
            for i in range(len(compt)):
                if compt[i] == score_max:
                    choix.append(i)
            nucl_max = random.choice(choix)
            seq_cons = seq_cons + nucl[nucl_max]
    return seq_cons

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

def reader(path_to_file, path_to_data):  #equivalent de tri_cle_valeur dans graph_input
    ref = sequences_reader(path_to_data)
    #print(ref)
    clusters = {}
    with open(path_to_file, "r") as file:
        for line in file:
            clust = line.strip().split()
            seqs = clust[1:]
            consensus = cons_bis(seqs, ref)
            if len(consensus) != 0:
                if len(consensus) not in clusters:
                    clusters[len(consensus)]={to_string(seqs) : consensus} # On fait comme pour tri_cle_valeur : dico de dico
                else :
                    clusters[len(consensus)][to_string(seqs)] = consensus
    #print(clusters)
    return clusters 

def distance_Hamming(seq1, seq2):
    distance=1
    for i in range (len(seq1)):
        if seq1[i]==seq2[i]: # Objectif : les séquences identiques soient plus liées entre elles que les séquences différentes
            distance +=1
    distance = distance / len(seq1)
    return(distance)
    
    
def distance_seqs(S1,S2):
    with open(pwd + '/seq1.fa', "w") as fichier1:
        fichier1.write('>S1\n'+S1)
    with open(pwd + '/seq2.fa', "w") as fichier2:
        fichier2.write('>S2\n'+S2)
    subprocess.run(["stretcher", "seq1.fa", "seq2.fa", "score.txt"], capture_output = True)
    with open(pwd + '/score.txt', 'r') as fichier:
        for line in fichier:
            if line.startswith('# Score'):
                score = line.strip().split()[2]
                #print(score)
                os.system('rm seq1.fa seq2.fa score.txt')
                return int(score)
    return 0

def instanciation_des_graphes_cle_valeur(dico): #prends en entrée un dictionnaire avec des sequences
	res = {}
	d2 = copy.deepcopy(dico) #copie indépendante de l'entrée
	count = 0
	c1 = 0
	c2 = 0
	for w in dico.keys():
		#print('longeur : ', w)
		count +=1
		G_courant = nx.Graph()
		for x in dico[w].keys():
			#print('\n\n', c1)
			c1 +=1
			c2 = 0
			seq = d2[w].pop(x) # d2 mémorise les séquences non parcourues
			G_courant.add_node(x) #certaines séquences sont les seules de leur taille
			for y in d2[w].keys() : #on ne calcule la distance que pour les séquences non parcourues 
				#print('c2', c2)
				c2 +=1
				d = distance_Hamming(dico[w][y], seq)
				G_courant.add_edge(x,y)
				G_courant[x][y]['weight'] = d
		res[w] = G_courant
	return res #retourne un dictionnaire de graphes


def generate_graphs_consensus(path_to_file,path_to_data):
	return instanciation_des_graphes_cle_valeur(reader(path_to_file,path_to_data))
	#return reader(path_to_file, path_to_data)
	
	
	
	
	
	
	
	
def main():
    #print(alignement(nucleotides,1,-2,'catgac','tctgaac',-1))
    res = generate_graphs_consensus("/home/lisa/Programmation/cloneCluster/data/Tools_output/IMGT_output/Real_data/I1_IMGT_Fo.txt", "/home/lisa/Programmation/cloneCluster/data/Real/Extracted_CDR3/Extracted_by_IMGT/I1_oligo_CDR3_NA.txt")
    #print(res)
    
if __name__ == "__main__":
    main()



