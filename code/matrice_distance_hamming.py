input = 'monoclonal_simp_indel_cdr3.fa'
Set = []
with open(input, "r") as fasta_file:
    for line in fasta_file:
        if not line.startswith(">"):
            Set.append(line.strip()) 

#Set contient toutes les séquences, il faut maintenant les trier par tailles
Dico = {}
for s in Set :
	if len(s) not in Dico :
		Dico[len(s)] = [s]
	else :
		Dico[len(s)].append(s)

print(Dico)

def distance_Hamming(seq1, seq2):
    distance=0
    for i in range (len(seq1)):
        if seq1[i]!=seq2[i]:
            distance +=1
    return(distance)

import numpy as np
def matrice_adjacence_Hamming(Longueur_seq):
    L=Dico[Longueur_seq]
    M=np.zeros((len(L), len(L)))
    for i in range (len(L)):
        for j in range (len(L)):
            M[i][j]=distance_Hamming(L[i], L[j])
    return(M)


for w in Dico.keys():
    print("Matrice de distances de Hamming pour les", len(Dico[w]), "séquences de longueur ",w,"\n",matrice_adjacence_Hamming(w),"\n")
