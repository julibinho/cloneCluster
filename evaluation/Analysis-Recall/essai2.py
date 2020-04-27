#! /usr/bin/env python3
# coding: utf-8
import argparse
import sys
from optparse import OptionParser
from decimal import Decimal


# =============================================================================
#               evaluate Measures
# =============================================================================		
def evaluateMeasures(cluster, hashCluster, totalSeq , hashCluster_detail, true_cluster): #hashcluster = true cluster, les clés sont les séquences
	count = 0; tp = 0; sumTp = 0.0; sumFp = 0.0; sumFn = 0.0; sumTtC = 0; tn = 0; sumTn = 0.0;
	countSeq = 0
	true_p = {}
	false_n = {}
	for i in cluster:
		count +=1
		if (count % 5000 == 0): print("Processed "), count
		arraySeqIds = cluster[i]
		#find the majority label
		hashAux = {}; tp = 0;
		for j in arraySeqIds:
			countSeq += 1
			if j.rstrip() in hashCluster_detail.keys(): # pour vérifier si la séquence à bien été classée par l'algo de clustering
				IDmember = hashCluster_detail[j.rstrip()] #IDmember = cluster dans le fichier true cluster
				if IDmember in hashAux.keys():
					hashAux[IDmember] += 1
				else:
					hashAux[IDmember] = 1

				maxValue = 0; maxLabel = ""
				if len(hashAux) != 0:
					#print hashAux
					for d in hashAux:
						#print d,"d"
						if hashAux[d] > maxValue:
							maxValue = hashAux[d]
							maxLabel = d # on cherche le cluster de référence dans le fichier true cluster
		for j in true_cluster[maxLabel] : #on récupère toutes les séquences du vrai cluster
			if j.rstrip() not in arraySeqIds : # on a trouvé un faux négatif
				if i not in false_n.keys():
					false_n[i] = [j.rstrip()]
				else :
					false_n[i].append(j.rstrip())
			else : #on a trouvé un vrai positif
				if i not in true_p.keys():
					true_p[i] = [j.rstrip()]
				else :
					true_p[i].append(j.rstrip())
		for j in arraySeqIds:
			if j.rstrip() in hashCluster_detail.keys():
				IDmember = hashCluster_detail[j.rstrip()]
				#print IDmember,"IDmember"
				if IDmember !="" and IDmember == maxLabel: #notre séquence 
					tp +=1

		totalCluster = hashCluster[maxLabel]
		
		sumTtC += totalCluster
		fn = totalCluster - tp
		#print('cluster n : ', i)
		#print(fn)
		#if i in false_n.keys():
		#	print(fn,  len(false_n[i]))
		
		#print(tp)
		#if i in true_p.keys() :
		#	print( tp, len( true_p[i]))
		if fn<0:
			print("erreur")
		fp = len(arraySeqIds) - tp
		tn = totalSeq -(tp+ fn +fp)
		sumTp += tp; sumFp += fp; sumFn += fn; sumTn += tn;
	print ('nombres de paires classees : ',sumTp+ sumFp+ sumFn+ sumTn)
	print('false negative : ', sumFn)
	print('true positive : ', sumTp )
	pre = sumTp/float(sumTp+ sumFp);
	rec = sumTp/float(sumTp+ sumFn);
	spe = sumTn/float(sumTn + sumFp)
	print ("Pre = ", round(pre,2), "Rec = ", round(rec,2) , "specificity = ",round(spe,2),"F-score = ", round(2*pre*rec/(pre + rec),2), "NumCluster = ", count, "NumSeqs = ", countSeq, " sumTtC = ", sumTtC)

	return true_p, false_n
# =============================================================================
#               Read data file (fasta)
# =============================================================================		
def readFasta(path_to_file):
	dico = {}
	count = 0
	with open(path_to_file, "r") as fasta_file:
		for line in fasta_file:
			if line.startswith(">"):
				count += 1
				name = line.strip()[1:]
			else:
				seq = line.strip()
				dico[name] = [seq, len(seq)]
	return dico #rend un dictionnaire avec l'id des seq comme clés, et une liste [sequence, longeur de la séquence] comme valeur;  
	
		
	
# =============================================================================
#             Analyse the différence between the false positiv seqs, 
#                          and the true positive seqs
# =============================================================================	
def analysis(seq, TP, FN):
	# Longeurs ??
	somme_fn = 0
	somme_fn_same_size = 0
	somme_same_size_32 = 0
	for i in FN.keys(): # on s'interesse surtout aux faux négatifs qui influent beaucoup sur le recall
		longueurs = {}
		for s in FN[i]:
			somme_fn +=1
			if len(seq[s][0]) in longueurs.keys():
				longueurs[len(seq[s][0])] += 1
			else :
				longueurs[len(seq[s][0])] = 1
		dict = {len(seq[TP[i][0]][0]) : len(TP[i])}
		if len(seq[TP[i][0]][0]) in longueurs.keys():
			if len(seq[TP[i][0]][0]) == 32:
				somme_same_size_32 += longueurs[len(seq[TP[i][0]][0])] 
			somme_fn_same_size += longueurs[len(seq[TP[i][0]][0])] 
		#print('\nlongueur TP :', dict ,'\nlongueur FN :', longueurs)
	print('\nfinalement, on trouve ', somme_fn_same_size, 'sequences mal classées alors qu\'elles ont la même taille que les tp, sur ', somme_fn, ' fn')
	#print('pour la taille 32 : ', somme_same_size_32)


# =============================================================================
#               Read cluster result formatted file
# =============================================================================	
def readResultFile(filename):
	cluster = {}; count = 0; totalSeq = 0;
	file = open(filename, "r")
	for line in file.readlines(): 
		#print line.split('\t')
		a=line.split('\t')
		count +=1
		if (count % 5000 == 0): print ("Processed ", count)
		IDcluster = int(a[0])
		members = a[1]

		#print len(members),"members"
		if (members == "\n" or members == ""):
			print ("Warnning:: Cluster ", IDcluster, " has no members")
		else: 
			#delet /n at the end of each line
			arraySeqIds = members.split(" ")
			if arraySeqIds[-1] == '\n':
				arraySeqIds = members.split(" ")[:-1]
			for i in range(len(arraySeqIds)):
			    if not arraySeqIds[i].startswith('S'):
			        arraySeqIds[i] = 'S' + arraySeqIds[i]
			if len(arraySeqIds) != 0:
				cluster[IDcluster] = arraySeqIds
				totalSeq += len(arraySeqIds)
	file.close()
	print ("Total clusters = ", count," Total sequences = " , totalSeq)
	return  cluster,totalSeq
	
# =============================================================================
#               Read true cluster file
# =============================================================================	
def readTrueClusterFile(filename):
	hashCluster = {}; count = 0; countCluster = 0;
	hashCluster_detail = {}
	file = open(filename, "r")
	for line in file.readlines(): 
		IDcluster = int(line.split('\t')[0].rstrip())
		seq = line.split('\t')[1].split(" ")
		seq[-1] = seq[-1].rstrip()
		#print seq
		for s in seq:
			#hashCluster_detail[int(s)] = IDcluster
			if not s.startswith("S"):
			    s = 'S' + s
			hashCluster_detail[s] = IDcluster
		hashCluster[int(IDcluster)] = len(seq)
	file.close()
	#print hashCluster,"hashclister"
	return  hashCluster, hashCluster_detail

#=============================================================================#
def main():
    usage = "python  cluster_based_fscore.py -p <clustering output> -t <true cluster file>\n "
    parser = OptionParser(usage)
    parser.add_option("-p", "--Predicted_clusters_File", dest="Predicted_clusters_File",
          help="read clusters from Predicted_File")
    parser.add_option("-t", "--True_clusters_file", dest="True_clusters_file",
          help="read data from True clusters file")
    parser.add_option("-d", "--data_file", dest="data_file", 
          help="read the fasta file of the sequences")
    
    (options, args) = parser.parse_args()
    #if len(sys.argv) != 6:
    #    parser.error("incorrect number of arguments")
    
    Predicted_File = options.Predicted_clusters_File
    True_file = options.True_clusters_file
    data_file = options.data_file
    cluster,totalSeq = readResultFile(Predicted_File)
    hashCluster , hashCluster_detail = readTrueClusterFile(True_file)
    true_c, tot = readResultFile(True_file)# on veut aussi les true cluster sous le format { n°cluster : [seqs]}
    seq = readFasta(data_file)
    
    TP , FN = evaluateMeasures(cluster, hashCluster, totalSeq, hashCluster_detail, true_c)
    print('\nAnalyse : ')
    analysis(seq, TP,FN)

#=============================================================================#
if __name__ == "__main__":
    main()
