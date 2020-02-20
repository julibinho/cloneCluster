#! /usr/bin/env python3
# coding: utf-8
import argparse

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-p","--path_to_file",help="""Chemin vers le fichier à utiliser""")
	parser.add_argument("-r","--result",help="""Ou doit-on ranger le résultat ?""")
	return parser.parse_args()




def read_seq_num(filename): #renvoie un dictionnaire séquence : numéro de cluster
	hashCluster = {}; count = 0; countCluster = 0;
	hashCluster_detail = {}
	file = open(filename, "r")
	for line in file.readlines(): 
		IDcluster = int(line.split('\t')[0].rstrip())
		seq = line.split('\t')[1].split() #seq = line.split('\t')[1].split(" ")
		#seq[-1] = seq[-1].rstrip() #########################
		for s in seq:
			#hashCluster_detail[int(s)] = IDcluster
			hashCluster_detail[s] = IDcluster
		hashCluster[int(IDcluster)] = len(seq)
	file.close()
	return  hashCluster_detail



def read_num_liste_seq(filename): #renvoie un dictionnaire numéro de cluster : list de séquences
	cluster = {}; count = 0; totalSeq = 0;
	file = open(filename, "r")
	for line in file.readlines(): 
		a=line.split('\t')
		count +=1
		if (count % 5000 == 0): print ("Processed ", count)
		IDcluster = int(a[0])
		members = a[1]
		if (members == "\n" or members == ""):
			print ("Warnning:: Cluster ", IDcluster, " has no members")
		else: 
			#delet /n at the end of each line
			arraySeqIds = members.split() #arraySeqIds = members.split(" ")[:-1]
			if len(arraySeqIds) != 0:
				cluster[IDcluster] = arraySeqIds
				totalSeq += len(arraySeqIds)
	file.close()
	return  cluster#,totalSeq


def find_false_negative(trueC,myC):#cherche les séquences qui devraient être dans le même cluster et qui ne le sont pas
	res_FN = []
	res_TP = []
	s = 0
	clust = 0
	seqs = 0
	for w in trueC.keys(): # on parcours les séquences en fonction de leurs appartenance au même cluster dans true cluster
		clust +=1
		temp = []
		cmp = 0
		for i in range(len(trueC[w])):
			seqs +=1
			temp.append(myC[trueC[w][i]])
			for j in range(i+1,len(trueC[w])):
				s +=1
				if myC[trueC[w][i]] != myC[trueC[w][j]]:
					cmp +=1
					res_FN.append((trueC[w][i],trueC[w][j]))
				else:
					res_TP.append((trueC[w][i],trueC[w][j]))
		#print(cmp,temp, '\n')
	print('faux négatifs trouvé',len(res_FN))
	print('vrai positifs trouvé',len(res_TP))
	#print('nombre d\'itérations : ', s)
	print('recall : ' ,len(res_TP)/(len(res_TP)+len(res_FN)))
	#print("nombre de séquences parcourues dans false neg : ", seqs, ' et nb de clust', clust)
	return (res_FN,res_TP)

def precision(trueC,myC):#cherche les séquences qu'on prédit dans le même cluster et qui ne le sont pas.
	res_FP = []
	res_TP = []
	s = 0
	seqs = 0
	for w in myC.keys(): # on parcours les séquences en fonction de comment elles ont étées classées par l'algo
		
		temp = []
		cmp = 0
		for i in range(len(myC[w])):
			seqs +=1
			temp.append(trueC[myC[w][i]]) # on ajoute le vrai cluster de la séquences à la liste de tous les vrai cluster des séquences de ce cluster calculé
			for j in range(i+1,len(myC[w])):
				s +=1
				if trueC[myC[w][i]] != trueC[myC[w][j]]:
					cmp +=1
					res_FP.append((myC[w][i],myC[w][j])) # les deux séquences sont classées dans le même cluster mais en réalité elle n'appartiennent pas au même cluster, donc c'est un faux positif
				else:
					res_TP.append((myC[w][i],myC[w][j])) # ici on obtiens les vrai positifs, qui sont dans le même cluster quoiqu'il arrive
		#print(cmp,temp, '\n')
	print('faux positifs trouvé',len(res_FP))
	print('vrai positifs trouvé',len(res_TP))
	#print('nombre d\'itérations : ', s)
	#print(seqs)
	print('precision : ' ,len(res_TP)/(len(res_TP)+len(res_FP)))
	return (res_FP,res_TP)
	

def main():
	args = parse_arguments()
	path_to_file = args.path_to_file
	path_to_result = args.result
	true_cluster= read_num_liste_seq(path_to_file) #true cluster indicé par les numéro de clusters
	inferred_cluster = read_seq_num(path_to_result) #inffered cluser indicé par les séquence
	#inferred_cluster.pop('')
	T_seq = read_seq_num(path_to_file)
	I_num = read_num_liste_seq(path_to_result)
	
	FP,TP_prec = precision(T_seq,I_num)
	
	print('\n')
	#print('taille de inferred_cluster',len(inferred_cluster))
	FN,TP_recall = find_false_negative(true_cluster, inferred_cluster)

	
	#print('\n\n\n\nTravail sur une sous liste:')
	
	#L = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 27, 31, 31, 0, 0, 0, 0, 0, 42, 0, 0, 0, 0, 0, 34, 34, 0, 9, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 6, 0, 0, 0, 41, 0, 0, 0, 0, 0, 33, 0, 0, 0, 0, 0, 0, 0, 25, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 34, 0, 0, 34, 33, 0, 0, 33, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 36, 0, 0, 36, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 34, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 0, 0, 28, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 6, 0, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 35, 0, 23, 0, 0, 0, 0, 0, 0, 0, 23, 0, 0, 6, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 40, 40, 0, 3, 42, 0, 0, 3, 0, 0, 0, 33, 33, 0, 0, 6, 0, 3, 0, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41, 4, 0, 0, 0, 0, 41, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 35, 0, 0, 0, 0, 0, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 23, 23, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 0, 27, 27, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 50, 3, 0, 0, 0, 9, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 34, 0, 28, 0, 0, 6, 3, 0, 0, 0, 0, 0, 3, 47, 47, 0, 47, 0, 0, 0, 0, 0, 0, 0, 0, 23, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 0, 3, 3, 3, 3, 3, 3, 6, 0, 0, 0, 47, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 34, 23, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 27, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 33, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 3, 3, 3, 3, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 0, 41, 0, 0, 0, 0, 0, 0, 0, 0, 41, 0, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 0, 0, 0, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  #cette matrice représente le monocluster de true cluster, et chaque valeur est le cluster d'appartenance de la séquence dans le résultat de l'algorithme. rien que pour ce cluster je trouve 74891 faux negatifs, et 170459 vrai positifs.
	#a = L.count(0)
	#print('valeurs identiques, valeurs différentes, total ',a,len(L)-a,len(L))
	#fn = 0
	#tp = 0
	#for i in range(len(L)) :
	#	for j in range(i+1,len(L)):
	#		if L[i] != L[j] :
	#			fn +=1
	#		else : 
	#			tp +=1
	#print('fn pour L uniquement ', fn)
	#print('tp pour L uniquement ', tp)

	#print(true_cluster,'\n\n\n',inferred_cluster,'\n\n\n',T_seq,'\n\n\n',I_num)
	#	print(len(true_cluster),'\n\n\n',len(inferred_cluster),'\n\n\n',len(T_seq),'\n\n\n',len(I_num))

if __name__ == "__main__": 
	main()

