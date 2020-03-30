#! /usr/bin/env python3
# coding: utf-8


################################################################
#   lit les fichiers résultats de Fair
################################################################
nucleotides = ['A','C','G','T']

def cons(l_seqs):
    N = len(l_seqs)
    res = [[1,1,1,1] for i in range(N)]
    for seq in l_seqs:
        for i in range(len(seq)):
            res[i][nucleotides.index(seq[i])] +=1
            
    for i in range(N):
        for j in range(len(res[i])):
            res[i][j] = res[i][j]/ N # on normalise le résultat
    return res
    

def reader(path_to_file): #TODO : il faut utiliser aussi la data pour connaitre la séquence correspondante
	clusters = {}
	with open(path_to_file, "r") as file:
		for line in file:
		    clust = line.strip()
		    num = clust[:1]
		    seqs = clust[2:]
		    print('\n\n',seqs)
		    clusters[num]=cons(seqs) # retourne la séquence consensus d'un cluster
			
	return dico 
	
def main():
    res = reader("/home/lisa/Programmation/cloneCluster/result/Artificial/Extracted_CDR3/(avant_opti)monoclonal_simp_indel_cdr3.txt")
    
if __name__ == "__main__":
    main()

