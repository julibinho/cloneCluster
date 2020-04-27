#! /usr/bin/env python3
# coding: utf-8
def resultat_pour_une_partition(part, i_min): # format d'un partition: num cluster : liste des seqs
    res = ''
    for w in set(part.values()) :
            res += "%i" % (i_min + w) + "\t"
            list_nodes = [nodes for nodes in part.keys() if part[nodes] == w]
            list_nodes.sort()
            for x in list_nodes :
                res += x + " "
            res += "\n"
    #print res
    return res

def generate_output_text(dico, path): #rassemble toutes les partitions
    count = 0
    with open(path, "w" ) as fichier :
        for w in dico.keys() :
            n = len(set(dico[w].values())) #nombre de clusters dans cette partition
            fichier.write(resultat_pour_une_partition(dico[w],count))
            count += n
    fichier.close()
    pass 




def read_fasta(path_to_file):
    seq = []
    with open(path_to_file, "r") as fasta_file:
        for line in fasta_file:
            if line.startswith(">"):
                seq.append(line.strip()[2:])
            
    return seq

def read_cluster(path_to_file):  #equivalent de tri_cle_valeur dans graph_input
    clusters = []
    with open(path_to_file, "r") as file:
        for line in file:
            clust = line.strip().split()
            seqs = clust[1:]
            clusters.append(seqs)
    return clusters 

def cleaner(seq,clusters): # retourne une partition avec uniquement les séquences connues
    #Partition: {taille : {seq : cluster}}
    count = 0
    partition = {}
    for c in clusters :
        for s in c:
            if s in seq:
                partition[s] = count
        count +=1 
    return {0:partition} #artifice pour avoir le même format que Louvain, et utiliser les algo de sortie texte. 

# I3_mono_CDR3_AA.txt  I4_poly_CDR3_AA.txt
#   I4_poly_CDR3_NA.txt
def main():
    fasta_path = "/home/lisa/Programmation/cloneCluster/data/Real/Extracted_CDR3/Extracted_by_IMGT/I4_poly_CDR3_NA.txt"
    cluster_path = "/home/lisa/Programmation/cloneCluster/data/Tools_output/IMGT_output/Real_data/I4_IMGT_Fo.txt"
    result_path ="/home/lisa/Programmation/cloneCluster/data/Tools_output/IMGT_output/Real_data/I4_IMGT_Fo_cleaned.txt" 
    seq = read_fasta(fasta_path)
    cluster = read_cluster(cluster_path)
    
    generate_output_text(cleaner(seq,cluster), result_path)



if __name__ == "__main__": 
    main()
