# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 11:21:19 2020

@author: quent
"""
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import kneighbors_graph
import math as math
import numpy as np
import copy
from sklearn.metrics import pairwise_distances_argmin
import os
import sys
pwd = os.getcwd()
sys.path.append(pwd+'/tool') # Fonctionne sur windows et linux, et permet d'indiquer dans quel fichier sont les modules. 
import argparse
import graph_input
#=======================================================
def initialisation(M):
    S=graph_input.matrice_adjacence_Hamming(M)
    d=[]
    for i in range (len(S)):
        degree=np.sum(S,axis=0)[i]
        d.append(degree)
    D=np.diag(d)
    return(S,D)
#==========================================================
def normalize(S,D):
    D=np.array(D)
    for i in range (len(D)):
        for j in range (len(D)):
            if D[i][j]!=0:
                D[i][j]=(D[i][j])**(-1/2)
    S=np.array(S)
    SD=np.dot(S,D)
    result=np.dot(D,SD)
    return(np.array(result))
#===========================================================
def eigen(M):
    vals,vect=np.linalg.eig(M)
    vals=np.real(vals)
    vals=np.sort(vals) #On trie de manière croissante les valeurs propres obtenues
    vect=np.real(vect)
    vals=np.array(vals)
    vect=np.array(vect)
    return(vals,vect)
#===========================================================
def renormalize(U):
    Y=np.zeros((len(U),len(U)),dtype=np.float)
    for i in range (len(U)):
        for j in range (len(U)):
            Y[i][j]=U[i][j]/((sum((U[i]**2)))**0.5)
    return(Y)
#===========================================================
def find_clusters(X, n_clusters, rseed=2):
    # 1. Randomly choose clusters
    rng = np.random.RandomState(rseed)
    i = rng.permutation(X.shape[0])[:n_clusters]
    centers = X[i]
    
    while True:
        # 2a. Assign labels based on closest center
        labels = pairwise_distances_argmin(X, centers)
        
        # 2b. Find new centers from means of points
        new_centers = np.array([X[labels == i].mean(0)
                                for i in range(n_clusters)])
        
        # 2c. Check for convergence
        if np.all(centers == new_centers):
            break
        centers = new_centers
    return centers, labels
#============================================================
def generate_output_text_SC(dico,path): #rassemble toutes les partitions
    with open(path, "w+" ) as fichier :
        count=0
        for w in dico.keys() :
            for i in dico[w].values():
                fichier.write(str(count))
                fichier.write("\t")
                for j in i:
                    fichier.write(j)
                    fichier.write(" ")
                count+=1
                fichier.write("\n")
        fichier.close()
        pass
#==================================================================
def k_nearest(D):
    graph=kneighbors_graph(D,3)
    return(graph)
#============================================================
def principale (L,nb_cluster,dico): #retourne les clusters pour une longueur L de séquence souhaitée
    sequences=[]
    for p in dico[L].keys():
        sequences.append(dico[L][p])
    sequences =np.array(sequences)
    nb_sequences=len(sequences)
    Adj,Diag=initialisation(sequences)
    Laplacian=normalize(Adj,Diag)
    Vals,Vect=eigen(Laplacian)
    Y=[]
    for i in range (len(Vals)-550):
        Y.append(i)
    if L==50:
        plt.scatter(Y,Vals[0:len(Vals)-550])
        plt.show()
    renorm=renormalize(Vect)
    #print(Vals)
    Centres,Cluster=find_clusters(renorm,nb_cluster)
    return(L,nb_sequences,Centres,Cluster)
    
    
def main():
    pass

if __name__ == "__main__":
    
    main()