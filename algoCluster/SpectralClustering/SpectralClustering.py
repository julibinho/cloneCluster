# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 11:33:30 2020

@author: quent
"""
import matplotlib.pyplot as plt
import math as math
import numpy as np
import copy
from sklearn.metrics import pairwise_distances_argmin
import os
import sys
pwd = os.getcwd()
sys.path.append(pwd+'/tool') # Fonctionne sur windows et linux, et permet d'indiquer dans quel fichier sont les modules. 
import argparse
import SpectralClusteringTools
import graph_input

##############################################################
#   Début du code 
##############################################################
def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-p","--path_to_file",help="""Chemin vers le fichier à utiliser""")
	parser.add_argument("-r","--result",help="""Ou doit-on ranger le résultat ?""")
	return parser.parse_args()

############################################################
#              MAIN
#############################s##############################
def main():
    args = parse_arguments()
    path_to_file = args.path_to_file
    path_to_result = args.result
    
    dico_sequences_in= graph_input.tri_cle_valeur(path_to_file)
    dico_partitions_out={}
    numero_cluster=0#Pour la construction des clé du dictionnaire outpout
    K_cluster=0 #Nombre de cluster souhaités en fonction du nombre de séquences pour chaque longueur
    for longueur in dico_sequences_in.keys():#Parcours du dico des séquences par les différentes clés = longueur de séquence
        #print(len(dico_sequences_in[longueur]))
        K_cluster=int(math.log(len(dico_sequences_in[longueur]),2))
        if K_cluster < 1:
            K_cluster = 1
        if longueur == 50 :
            K_cluster = 4
        #print(K_cluster)
        L,nb_sequences,Centres,Cluster=SpectralClusteringTools.principale(longueur,K_cluster,dico_sequences_in)
        keys=[]
        for nom_seq in dico_sequences_in[longueur].keys(): #Parcours des différents noms de séquences appartenant à la longueur k en cours
            keys.append(nom_seq)
        #print("keys",keys)
        dico_partitions_out[longueur]={}#On crée un nested dictionnary pour pouvoir ensuite append les valeurs qui nous intéressent
        for centre_chercher in range (len(Centres)): #Parcours des différents Centres (= N° des clusters)
            dico_partitions_out[longueur][numero_cluster]=[]#On initialise le nested dictionnary pour pouvoir ensuite append les valeurs qui nous intéressent
            for l in range (len(keys)): #Parcours de la liste associant un cluster pour chaque point
                if Cluster[l]==centre_chercher:
                    (dico_partitions_out[longueur][numero_cluster]).append(keys[l])
            numero_cluster+=1
    SpectralClusteringTools.generate_output_text_SC(dico_partitions_out,path_to_result)

if __name__ == "__main__":
    main()