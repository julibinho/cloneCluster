#! /usr/bin/env python3
# coding: utf-8

import time
import essai
import tri_des_seq as tri
import matrice_distance_hamming as matHamming

# Debut du decompte du temps
#start_time = time.time()
#dico_des_sequences = tri.tri_cle_valeur('/home/lisa/Programmation/cloneCluster/data/artficial/Extracted_CDR3/monoclonal_simp_indel_cdr3.fa') #trie les séquences par tailles
#dico_des_graphes = matHamming.instanciation_des_graphes_cle_valeur(dico_des_sequences)
# Affichage du temps d execution
#print("Temps d execution : %s secondes ---" % (time.time() - start_time))




start_time_e = time.time()
dico_des_graphes = essai.generate_graph('/home/lisa/Programmation/cloneCluster/data/artficial/Extracted_CDR3/monoclonal_simp_indel_cdr3.fa')
# Affichage du temps d execution
print("Temps d execution d'essai : %s secondes ---" % (time.time() - start_time_e))
