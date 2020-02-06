# -*- coding: utf-8 -*-

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

	

