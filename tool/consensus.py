#! /usr/bin/env python3
# coding: utf-8


################################################################
#   lit les fichiers résultats de Fair
################################################################
nucleotides = ['a','c','g','t']

###############################################################
#                      Alignement des séquences
#             Needleman et Wunsch
###############################################################

def matrice_des_distances(alphabet, match, mismatch):
    res = [[mismatch for i in range(len(alphabet))] for j in range(len(alphabet))]
    for i in range(len(alphabet)):
        res[i][i]= match
    return res

def matrice_scores(alphabet, match, mismatch,s1,s2,gap): 
    #complexité quadratique, car on remplis la matrice case par case avec deux boucles for
    mat_sc = matrice_des_distances(alphabet,match,mismatch)
    n = len(s1)+1
    m = len(s2)+1
    res = [[0 for j in range(n)] for i in range(m)]
    T = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        res[i][0] = i * gap
    for j in range(n):
        res[0][j] = j* gap
    for j in range(1,n):
        for i in range(1,m):
            a = res[i-1][j-1] + mat_sc[index(nucleotides,s2[i-1])][index(nucleotides,s1[j-1])]
            b = res[i-1][j] + gap
            c = res[i][j-1] + gap
            res[i][j] = max(a,b,c)
            T[i][j] = traceback(a,b,c)
    return res, T

def traceback(a,b,c): 
    #la stratégie de recomposition des séquences est choisie ici, 
    #puisqu'on favorise en premier les transitions en diagonale, 
    #puis en haut, et enfin si aucune des deux n'est possible, à gauche. 
    if (c > b) & (c > a):
        resb = 3
    if (b > a) & (b > c):
        resb = 2
    if (b == c) & (b > a):
        resb = 2
    if (a > b) & (a > c):
        resb = 1
    if (a == c) & (a > b):
        resb = 1
    if (a == b) & (a > c):
        resb = 1
    if (a == b) & (b == c):
        resb = 1
    return resb

def alignement(alphabet, match, mismatch,s1,s2,gap): 
    n = len(s1)+1
    m = len(s2)+1
    res,T = matrice_scores(alphabet,match,mismatch,s1,s2,gap)
    seq1 = []
    seq2 = []
    Max = -1000
    I = 0
    J = 0
    if(m > n):
        for i in range(m):
            if (res[i][n-1] > Max) :
                Max = res[i][n-1]
                I , J = i, n-1
    else :
        for j in range(n):
            if (res[m-1][j] > Max) :
                I , J = m-1, j
                Max = res[m-1][j]
    
    for i in range(min(n,m)):
        t = T[I][J]
        if t == 1 :
            seq1.append(s1[J-1])
            seq2.append(s2[I-1])
            I = I - 1
            J = J - 1
        elif t == 2 : 
            seq1.append(4)
            seq2.append(s2[I-1])
            I = I -1
        else : 
            seq1.append(s1[J-1])
            seq2.append(4)
            J = J -1
    for i in range(I):
        seq2.append(s2[i])
        seq1.append(4)
    for j in range(J):
        seq1.append(s1[j])
        seq2.append(4)
        
    #Les séquences sont retournées dans le mauvais sens, 
    #mais elles sont correctement alignées. Le caractère 4 est associé à un '_'
    return seq1, seq2 

def tri_des_seq_par_tailles(l_seqs): #prends la liste des séquences, pas des ID
    dico = {}
    for s in l_seqs:
        if len(s) not in dico:
            dico[len(s)] = [s]
        else :
            dico[len(s)].append(s)
    res = []
    for w in sorted(dico.keys()):
        res.extend(dico[w])
    #print(res)
    return res
    
def alignement_mult(l_seqs,alphabet, match, mismatch,gap): #prends une liste de séquences, et retourne les séquences alignées
    #print('nouveau cluster')
    l_seqs = tri_des_seq_par_tailles(l_seqs)
    res = []
    s0 = l_seqs[0]
    m = len(s0)#taille minimale des séquences
    for s1 in l_seqs[1:]:
        s_res_0, s_res_1 = alignement(alphabet, match, mismatch,s0,s1,gap)
        #print('s_res', s_res_0)
        res.append(coupe(s_res_0, m))
        s0 = s1
    #print(res)
    return res


def coupe(seq, taille):
    for n in seq :
        if n !=4:
            d = seq.index(n)
            break
    if d+taille < len(seq):
        return(seq[d:d+taille]) 
    else :
        print('problème d\'alignement')
        print(taille+d,len(seq),d)
        return seq 
    
##################################################################
#                   Lecture des fichiers de Fair
###################################################################
def index(l,elem):
    for i in range(len(l)):
        if l[i].lower() == elem.lower():
            return i
    return 0


def sequences_reader(path_to_file): 
	dico = {}
	with open(path_to_file, "r") as fasta_file:
		for line in fasta_file:
			if line.startswith(">"):
				name = line.strip()[1:]
			else:
				seq = line.strip()
				dico[name]=seq
	return dico # S1: 'AACC...

def taille_min(l_seqs,ref):
    res = len(ref[l_seqs[0]])
    for s in l_seqs[1:]:
        if len(ref[s]) < res :
            res = len(ref[s])
    return res


	
def cons(l_seqs, ref): #liste de séquences du cluster et dictionnaire de référence de toutes les séquences
    N = len(l_seqs) # nombres de séquences
    M = taille_min(l_seqs,ref) #longueur minimale des séquences
    res = [[0,0,0,0] for i in range(M)]
    l_seqs=[ref[ID] for ID in l_seqs]
    alignement_mult(l_seqs, nucleotides, 1,-2,-10)
    for seq in l_seqs:
        for i in range(M):
            res[i][index(nucleotides,seq[i])] +=1
            
    for i in range(M):
        for j in range(len(res[i])):
            res[i][j] = res[i][j]/ (N) # on normalise le résultat, 
            
    #print(res)
    return res
    

def reader(path_to_file, path_to_data): 
    ref = sequences_reader(path_to_data)
    clusters = {}
    with open(path_to_file, "r") as file:
        for line in file:
            clust = line.strip().split()
            num = clust[0]
            seqs = clust[1:]
            clusters[num]=cons(seqs, ref) # retourne la séquence consensus d'un cluster
    return clusters 

def main():
    #print(alignement(nucleotides,1,-2,'catgac','tctgaac',-1))
    
    
    res = reader("/home/lisa/Programmation/cloneCluster/data/Tools_output/IMGT_output/Real_data/I1_IMGT_Fo.txt", "/home/lisa/Programmation/cloneCluster/data/Real/EntireSeq/I1_oligo.fa")
    
if __name__ == "__main__":
    main()

