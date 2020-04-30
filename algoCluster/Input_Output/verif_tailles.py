#! /usr/bin/env python3
# coding: utf-8
import copy
import networkx as nx
import math
import align_mult
import os
pwd = os.getcwd()



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



def reader(path_to_file, path_to_data):  #equivalent de tri_cle_valeur dans graph_input
    ref = sequences_reader(path_to_data)
    #print(ref)
    clusters = {}
    with open(path_to_file, "r") as file:
        for line in file:
            clust = line.strip().split()
            seqs = clust[1:]
            clusters[clust[0]] = seqs # on fait la correspondance entre le num du cluster et les séquences   
    res = {}
    for l in clusters.keys():
        res[l] = verif_taille(clusters[l], ref)        
    return res

def verif_taille(clust, ref):
    res = {}
    res_exist = []
    for s in clust:
        if s[1:] in ref:
            s = s[1:]
        if 'S'+s in ref:
            s = 'S' + s
        if s in ref:
            taille = len(ref[s])
            if taille in res:
                res[taille].append(s)
            else :
                res[taille] = [s]
        else:
            res_exist.append(s)
    k = list(res.keys())
    if len(k) > 1:
        return (res, res_exist)
    else :
        return (0, res_exist)
        
def pretty_printer(dico, nom):
    with open(nom, 'w') as fichier:
        fichier.write('Problemes d\'existance des séquences : \n\n\n')
        for l in dico.keys():
            if dico[l][1] != []:
                #print('on trouve des séquences inexistantes')
                fichier.write('\ncluster ' + l + '\nles seqs n\'existent pas dans le fichier source :' + str(dico[l][1]))
        fichier.write('\n\n\nProblème de longueur des séquences d\'un même cluster : \n\n\n')
        for l in dico.keys():
            if dico[l][0] != 0:
                #print('on trouve des séquences pas de la bonne longueur', dico[l][0], l )
                fichier.write('\ndans le cluster ' + l + 'les seqs n\'ont pas toutes la même taille :')
                for w in dico[l][0].keys():
                    fichier.write('\n les sequences '+  str(dico[l][0][w])+ ' sont de la tailles ' + str(w))
        




def main():
    pretty_printer(reader(pwd +"/data/Tools_output/IMGT_output/Real_data/I1_IMGT_Fo.txt", pwd + "/data/Real/Extracted_CDR3/Extracted_by_IMGT/I1_oligo_CDR3_NA.txt"), pwd + "/result/Analyses/anomalies_sequences_I1_NA.txt")
if __name__ == "__main__":
    main()

