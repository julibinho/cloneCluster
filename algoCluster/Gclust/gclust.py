#-*-coding:utf8-*-
import os 
pwd = os.getcwd()
import argparse
import graph_input
import numpy as np
import random as rd
from sklearn import mixture
from pylab import *
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.ticker as mt
import cogent.app.muscle_v38 as muscle
from Bio import Entrez

def main ():
    args = parse_arguments()
    path_to_file = args.path_to_file
    path_to_result = args.result
    liste = path_to_file
    dico_des_mat_dist,dico_des_seqs=graph_input.generate_matrix(liste)
    for cle_courante in dico_des_mat_dist.keys():
        L = dico_des_mat_dist[cle_courante]
        L = np.asmatrix(L)
        groupes = Gclust(liste,drawgraphs=False) #,nbClusters='AIC')

    with open("PWD/result/Artificial/Gclust/CDR3/Clustering.txt", "r+") as fichier_bad:
        cmpt=0
        for line in fichier_bad:
            fichier_good = open (path_to_result, "a")
            line = str(cmpt) + '\t' + line
            line = line.replace('[','')
            line = line.replace(']','')
            line = line.replace(',','')
            line = line.replace("'",'')
            cmpt+=1
            fichier_good.write(line)
            fichier_good.close()
##############################################################
#   Starting code 
##############################################################
def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-p","--path_to_file",help="""Chemin vers le fichier à utiliser""")
	parser.add_argument("-r","--result",help="""Ou doit-on ranger le résultat ?""")
	return parser.parse_args()



#####################################################
## I)  Pretreatment, create a similarity matrix :
#####################################################


def distance(alignement1, alignement2, gapOpen = -10, gapExtend = -0.5):
    '''
    This function returns the distance between two aligned sequences. This function is a subfunction of "matriceDistances". 
    '''
    EDNAFULL = {'A': {'A': '5', 'C': '-4', 'B': '-4', 'D': '-1', 'G': '-4', 'H': '-1', 'K': '-4', 'M': '1', 'N': '-2', 'S': '-4', 'R': '1', 'T': '-4', 'W': '1', 'V': '-1', 'Y': '-4'}, 'C': {'A': '-4', 'C': '5', 'B': '-1', 'D': '-4', 'G': '-4', 'H': '-1', 'K': '-4', 'M': '1', 'N': '-2', 'S': '1', 'R': '-4', 'T': '-4', 'W': '-4', 'V': '-1', 'Y': '1'}, 'B': {'A': '-4', 'C': '-1', 'B': '-1', 'D': '-2', 'G': '-1', 'H': '-2', 'K': '-1', 'M': '-3', 'N': '-1', 'S': '-1', 'R': '-3', 'T': '-1', 'W': '-3', 'V': '-2', 'Y': '-1'}, 'D': {'A': '-1', 'C': '-4', 'B': '-2', 'D': '-1', 'G': '-1', 'H': '-2', 'K': '-1', 'M': '-3', 'N': '-1', 'S': '-3', 'R': '-1', 'T': '-1', 'W': '-1', 'V': '-2', 'Y': '-3'}, 'G': {'A': '-4', 'C': '-4', 'B': '-1', 'D': '-1', 'G': '5', 'H': '-4', 'K': '1', 'M': '-4', 'N': '-2', 'S': '1', 'R': '1', 'T': '-4', 'W': '-4', 'V': '-1', 'Y': '-4'}, 'H': {'A': '-1', 'C': '-1', 'B': '-2', 'D': '-2', 'G': '-4', 'H': '-1', 'K': '-3', 'M': '-1', 'N': '-1', 'S': '-3', 'R': '-3', 'T': '-1', 'W': '-1', 'V': '-2', 'Y': '-1'}, 'K': {'A': '-4', 'C': '-4', 'B': '-1', 'D': '-1', 'G': '1', 'H': '-3', 'K': '-1', 'M': '-4', 'N': '-1', 'S': '-2', 'R': '-2', 'T': '1', 'W': '-2', 'V': '-3', 'Y': '-2'}, 'M': {'A': '1', 'C': '1', 'B': '-3', 'D': '-3', 'G': '-4', 'H': '-1', 'K': '-4', 'M': '-1', 'N': '-1', 'S': '-2', 'R': '-2', 'T': '-4', 'W': '-2', 'V': '-1', 'Y': '-2'}, 'N': {'A': '-2', 'C': '-2', 'B': '-1', 'D': '-1', 'G': '-2', 'H': '-1', 'K': '-1', 'M': '-1', 'N': '-1', 'S': '-1', 'R': '-1', 'T': '-2', 'W': '-1', 'V': '-1', 'Y': '-1'}, 'S': {'A': '-4', 'C': '1', 'B': '-1', 'D': '-3', 'G': '1', 'H': '-3', 'K': '-2', 'M': '-2', 'N': '-1', 'S': '-1', 'R': '-2', 'T': '-4', 'W': '-4', 'V': '-1', 'Y': '-2'}, 'R': {'A': '1', 'C': '-4', 'B': '-3', 'D': '-1', 'G': '1', 'H': '-3', 'K': '-2', 'M': '-2', 'N': '-1', 'S': '-2', 'R': '-1', 'T': '-4', 'W': '-2', 'V': '-1', 'Y': '-4'}, 'T': {'A': '-4', 'C': '-4', 'B': '-1', 'D': '-1', 'G': '-4', 'H': '-1', 'K': '1', 'M': '-4', 'N': '-2', 'S': '-4', 'R': '-4', 'T': '5', 'W': '1', 'V': '-4', 'Y': '1'}, 'W': {'A': '1', 'C': '-4', 'B': '-3', 'D': '-1', 'G': '-4', 'H': '-1', 'K': '-2', 'M': '-2', 'N': '-1', 'S': '-4', 'R': '-2', 'T': '1', 'W': '-1', 'V': '-3', 'Y': '-2'}, 'V': {'A': '-1', 'C': '-1', 'B': '-2', 'D': '-2', 'G': '-1', 'H': '-2', 'K': '-3', 'M': '-1', 'N': '-1', 'S': '-1', 'R': '-1', 'T': '-4', 'W': '-3', 'V': '-1', 'Y': '-3'}, 'Y': {'A': '-4', 'C': '1', 'B': '-1', 'D': '-3', 'G': '-4', 'H': '-1', 'K': '-2', 'M': '-2', 'N': '-1', 'S': '-2', 'R': '-4', 'T': '1', 'W': '-2', 'V': '-3', 'Y': '-1'}}
    score = 0
    ali1, ali2 = list(alignement1), list(alignement2)
    k=0
    while k<len(ali1):
        if ali1[k] == ali2[k] == '-':
            del ali1[k]
            del ali2[k]
        else:
            k += 1
    scoreMax = 5 * len(ali1)
    for k in range(160,0,-1):
        l=0
        while l<len(ali1)-k+1:
            if ali1[l:l+k] == list('-'*k):
                score += gapOpen + gapExtend*k
                del ali1[l:l+k]
                del ali2[l:l+k]
            elif ali2[l:l+k] == list('-'*k):
                score += gapOpen + gapExtend*k
                del ali1[l:l+k]
                del ali2[l:l+k]
            else:
                l+=1
    for k in range(len(ali1)):
        score += eval(EDNAFULL[ali1[k]][ali2[k]])
    return float(scoreMax-score)/scoreMax


def matriceDistances(dicoMuscle , nc):
    '''
    This function is a subfunction of "similarity".
    Input:
    -dicoMuscle : A dictionary of sequences in which the keys are the names of the sequences.
    -nc : The names of the sequences.
    Output:
    -Matrix : A matrix of distance. 
    '''
    Matrix = []
    for cpt1, genome1 in enumerate(nc):
        ligne = []
        for cpt2, genome2 in enumerate(nc):
            if cpt1 > cpt2 :
                ligne.append(Matrix[cpt2][cpt1])
            else :
                ligne.append(distance(dicoMuscle[genome1],dicoMuscle[genome2]))
        Matrix.append(ligne)
    Matrix = np.asmatrix(Matrix)
    return Matrix

def similarity(liste):
    '''
    This function returns the similarity matrix.
    Input:
    -Liste : A list of sequences with their names (see example).
    Output:
    -MatSimil : The similarity matrix.
    -nc : The names of the sequences. 
    '''
    # I) First step : Apply
    #nc = [u.split('\n')[0] for u in liste.split('>')[1:]]
    nc=[]
    for i in dico_des_seqs[cle_courante].keys():
        nc.append(i)
    MatDistance = L
    Max = float(MatDistance.max())
    MatDistance = MatDistance / Max
    MatSimil = 1 - MatDistance
    MatSimil = np.nan_to_num(MatSimil)
    return MatSimil, nc


##################################################################
##  II) Subfunctions, apply laplacian and GMM, draw graphics :
##################################################################


def plotembedding(vecprop, p, AddToNamesOfOutputs) :
    '''
    This function allows us to represent the clusters on 2D graphs in the bases generated by eigenvectors.
    Input:
    - vecprop : The list of retained eigenvectors. (2,3 or 4 eigenvectors).
    - p : The clustering. Vector of size equal to the number of species in which each species is associated with its cluster.
    -AddToNamesOfOutputs : A character string that is inserted as prefix in the output filenames
    '''
    coord=[]
    coord.append(vecprop[0,:])
    coord.append(vecprop[1,:])
    
    if len(vecprop)>2:
        coord.append(vecprop[2,:])
    
    if len(vecprop)==4 :
        coord.append(vecprop[3,:])
    
    dicoCoul={0:'b',1:'r',2:'y',3:'c',4:'k',5:'m',6:'g',7:'c',8:'springgreen',9:'brown'}
    listCoul = []
    for i in range(len(p)):
        listCoul.append(dicoCoul[p[i]])
    scatter(coord[0],coord[1],color=listCoul) 
    xlabel('Component 1')
    ylabel('Component 2')
    plt.savefig(AddToNamesOfOutputs + 'eigenvectors_1_and_2.png')
    #title('GMM clustering with 2 eigenvectors')
    show()
    
    if len(vecprop)>2 :
        scatter(coord[0],coord[2],color=listCoul) 
        xlabel('Component 1')
        ylabel('Component 3')
        #title('GMM clustering with 2 eigenvectors')
        plt.savefig(AddToNamesOfOutputs + 'eigenvectors_1_and_3.png')
        show()
        scatter(coord[1],coord[2],color=listCoul) 
        xlabel('Component 2')
        ylabel('Component 3')
        plt.savefig(AddToNamesOfOutputs + 'eigenvectors_2_and_3.png')
        #title('GMM clustering with 2 eigenvectors')
        show()
    
    if len(vecprop)==4 :
        scatter(coord[0],coord[3],color=listCoul) 
        xlabel('Component 1')
        ylabel('Component 4')
        plt.savefig(AddToNamesOfOutputs + 'eigenvectors_1_and_4.png')
        #title('GMM clustering with 2 eigenvectors')
        show()
        scatter(coord[1],coord[3],color=listCoul) 
        xlabel('Component 2')
        ylabel('Component 4')
        plt.savefig(AddToNamesOfOutputs + 'eigenvectors_2_and_4.png')
        #title('GMM clustering with 2 eigenvectors')
        show()
        scatter(coord[2],coord[3],color=listCoul) 
        xlabel('Component 3')
        ylabel('Component 4')
        plt.savefig(AddToNamesOfOutputs + 'eigenvectors_3_and_4.png')
        #title('GMM clustering with 2 eigenvectors')
        show()


def plotMatrix(w, AddToNamesOfOutputs):
    '''
    This function plot the graphical representation of the similarity matrix.
    Input :
    -w: The similarity matrix
    -AddToNamesOfOutputs : A character string that is inserted as prefix in the output filenames
    '''
    (N, M) = w.shape 
    fig,ax=plt.subplots()
    exts = (0, M, 0, N)
    ax.imshow(w, interpolation='nearest', cmap=cm.autumn_r, extent=exts)
    cbar = fig.colorbar(ax.imshow(w, interpolation='nearest', cmap=cm.autumn_r, extent=exts), ticks=[0,1])
    cbar.ax.set_yticklabels(['0','1'])
    ax.xaxis.set_major_locator(mt.NullLocator())
    ax.yaxis.set_major_locator(mt.NullLocator())
    plt.savefig(AddToNamesOfOutputs + 'similarity_matrix.png')
    plt.show()


def Laplacian(w) :
    '''
    This function returns the normalized Laplacian associated with the similarity matrix.
    Input:
    -w: The similarity matrix
    Output :
    -The normalized Laplacian
    '''
    d=np.zeros((w.shape[0],w.shape[0]))
    for i in range(w.shape[0]) :
        for j in range(w.shape[0]) :
            d[i,i]=d[i,i]+w[i,j]        # d = matrix of degrees
    return(dot(np.linalg.pinv(d),d-w))


def chooseNbEigenvectors(vectOfEigenvalues, N, nbEVMethod, nbEVCutOff):
    '''
    This function allows us to determine the number of eigenvectors to keep according to the method chosen by the user.
    Input :
    -v : Vector of Eigenvalues
    -N : number of subjects
    -nbEVMethod: The method chosen to determine the number of Eigenvectors
    -nbEVCutOff: The Cut-off (when the method is 'delta' or 'energy') 
    Output
    -The number of Eigenvectors
    '''
    
    if (nbEVMethod == 'delta'):
        if (nbEVCutOff == 'default'):
            nbEVCutOff = 0.01
        i = 1
        if len(vectOfEigenvalues) <= 2:
            return(i)
        while (vectOfEigenvalues[i+1] > vectOfEigenvalues[i] + nbEVCutOff):
            i+=1
            if (i == (N-1)):
               break
    if (nbEVMethod == 'log'):
        i = round(log(N))
    if (nbEVMethod == 'energy'):
        if (nbEVCutOff == 'default'):
            nbEVCutOff = 0.9
        lambda_max = vectOfEigenvalues[N-1]
        reverse = lambda_max - vectOfEigenvalues
        SumTotal = sum(reverse) - lambda_max 
        Sum = reverse[1]
        i = 1
        while (Sum < nbEVCutOff * SumTotal):
            Sum += reverse[i+1]
            i+=1
    return i


def LaplacianAndGMM(w, refs, nbClusters, drawgraphs, nbEVMethod, nbEVCutOff, AddToNamesOfOutputs):
    '''
    This function executes the laplacian eigenmap and the GMM on a similarity matrix and returns the clustering.
    Input : 
    -  w : The similarity matrix
    - refs : sequences names
    -  nbClusters : Number of clusters to be considered for classification (by default, BIC criterion).
    -  drawgraphs : Boolean argument. If drawgraphs == True, the graphics are plotted.
    -nbEVMethod: The method chosen to determine the number of Eigenvectors
    -nbEVCutOff: The Cut-off (when the method is 'delta' or 'energy') 
    -AddToNamesOfOutputs : A character string that is inserted as prefix in the output filenames.
    Outupt :
    - groupes : The clustering.
    '''
    if len(w)==1:
        clusters=[]
        for i in range(1):
            clusters.append([])
        for i in range(1):
            clusters[0].append(refs[i])    
        clustersString = str(clusters[0]) +'\n'
        fichier = open(AddToNamesOfOutputs + 'Clustering.txt' , "a")
        fichier.write(clustersString)
        fichier.close()
        return clusters

    N = w.shape[0]
    
    if drawgraphs==True:
        plotMatrix(w, AddToNamesOfOutputs)
        
    Lrw = Laplacian(w)  ## Lrw is the normalized Laplacian
    
    vp=[]
    b=np.linalg.eig(Lrw)   
    for i in range(N) :
        Mat = b[1].T[i]
        X = Mat.tolist()
        X = X[0]
        b[0][i] = np.real(b[0][i])
        #print("c'est X",X)
        X = list(np.real(X))
        vp.append([b[0][i],X])

    VP=sorted(vp)    ## VP is the list of eigenvalues and eigenvectors sorted in )ascending order according to the eigenvalues.
    vaP= []
    for i in range(N) :
        vaP.append(VP[i][0])  ## vaP is the list of eigenvalues only (sorted in ascending order).

    if drawgraphs==True :
        nbPlotted = min(N,11) # Number of eigenvalues plotted
        title('Values of the ' + str(nbPlotted-1) +  ' smallest eigenvalues')
        plot(range(nbPlotted),vaP[0:(nbPlotted)])    
        show()

    i = chooseNbEigenvectors(vaP, N, nbEVMethod, nbEVCutOff)
    print "The " + str(i) + " first eigenvalues have been selected."
    
    vePclasses=[]
    for j in range(N):
        vePclasses.append(VP[j][1])
        
    vecprop=np.asarray(vePclasses[1:i+1])
    
    if (nbClusters=='BIC'):
        H1 = []
        for j in range(1,N+1) :
            gmm = mixture.GaussianMixture(n_components=j, covariance_type='full')
            h = gmm.fit(vecprop.T)
            H1.append(h.bic(vecprop.T))  
        k = argmin(H1)+1       # Number of clusters for optimal classification

    if (nbClusters=='AIC'):
        H1 = []
        for j in range(1,N+1) :
            gmm = mixture.GaussianMixture(n_components=j, covariance_type='full')
            h = gmm.fit(vecprop.T)
            H1.append(h.aic(vecprop.T))  
        k = argmin(H1)+1       # Number of clusters for optimal classification

    if (nbClusters != 'BIC' and nbClusters=='AIC'):
        k = nbClusters

    if (drawgraphs==True and (nbClusters=='BIC' or nbClusters=='AIC')) :
        Min = (max(0, k-5))
        Max = (min(N, k+5))
        plot(range(Min+1,Max+1),H1[Min:Max],label='full')
        if (nbClusters=='BIC'):
            title('Bayesian Information Criterion of the Gaussian Mixture Models \n')
        if (nbClusters=='AIC'):
            title('Akaike Information Criterion of the Gaussian Mixture Models \n')
        show()  
    
    Bic = float('inf')
    gmm = mixture.GaussianMixture(n_components = k, covariance_type='full') ### Ici il faut que je place une seed
    for i in range(20):
        h0 = gmm.fit(vecprop.T)
        B =  h0.bic(vecprop.T)
        if B < Bic:
            Bic = B
            h = h0

    p0 = h.predict_proba(vecprop.T)

    p = np.zeros(len(p0))
    for i in range(len(p0)):
        p[i] = argmax (p0[i])
    
    clusters=[]
    for i in range(k):
        clusters.append([])

    for i in range(N):
        clusters[int(p[i])].append(refs[i])

    clustersString = str(clusters[0])

    if w.all() == 0 and len(w)<=2:
        clustersString = str(clusters[0] +clusters[1]) +'\n'
        fichier = open(AddToNamesOfOutputs + 'Clustering.txt' , "a")
        fichier.write(clustersString)
        fichier.close()
        return clusters
    else:
        for i in range(1, k):
            clustersString =clustersString + '\n' + str(clusters[i])
        clustersString += '\n' 
        fichier = open(AddToNamesOfOutputs + 'Clustering.txt' , "a")
        fichier.write(clustersString)
        fichier.close()
        return clusters

    if drawgraphs==True :
        plotembedding(vecprop, p, AddToNamesOfOutputs)
    return clusters


#######################################################################################################
## III)  Gclust function : Gclust(liste ,nbClusters='BIC',drawgraphs=True,delta = 0.01)
#######################################################################################################


def Gclust(liste, nbClusters='BIC', drawgraphs=True, nbEVMethod = 'delta', nbEVCutOff = 'default', AddToNamesOfOutputs = ''):
    '''
    The main function.
    Input : 
    -  liste : A list of sequences with their names (see example).
    -  nbClusters : Number of clusters to be considered for classification (by default, BIC criterion).
    -  drawgraphs : Boolean argument. If drawgraphs == True, the graphics are plotted.
    -  delta : Criterion of selection of the number of eigenvectors to consider.
    Outupt :
    - groupes : The clustering.
    '''
    w, refs = similarity(liste)
    groupes = LaplacianAndGMM(w, refs, nbClusters, drawgraphs, nbEVMethod, nbEVCutOff, AddToNamesOfOutputs)
    return groupes



#########################################################################################
##### IV) Main function
#########################################################################################




if __name__ == "__main__":
    main()
