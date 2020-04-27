"""
Program for evaluate the clustring performance of different Rep-seq tools.
The calculated metrics are : Precision, recall, F-score and Specificity.
This evaluation if for simulated sequences for which we know the real clusters.
!!!! there is  a S at the beginign of the sequencene names wich are ommited in the IMGT output
!! TO DO !! modify the script of formating the output of IMGT, to add a 'S' at the begining of each sequence's name
"""

import sys
from optparse import OptionParser
from decimal import Decimal
# =============================================================================
#               evaluate Measures
# =============================================================================		
def evaluateMeasures( cluster, hashCluster, totalSeq , hashCluster_detail) :
	#print cluster
	#print hashCluster_detail,"hashCluster_detail"
	count = 0; tp = 0; sumTp = 0.0; sumFp = 0.0; sumFn = 0.0; sumTtC = 0; tn = 0; sumTn = 0.0;
	countSeq = 0

	for i in cluster:
		count +=1
		if (count % 5000 == 0): print("Processed "), count
		arraySeqIds = cluster[i]
		#find the majority label
		hashAux = {}; tp = 0;
		for j in arraySeqIds:
			countSeq += 1
			if j.rstrip() in hashCluster_detail.keys():
				IDmember = hashCluster_detail[j.rstrip()]
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
							maxLabel = d
		for j in arraySeqIds:
			if j.rstrip() in hashCluster_detail.keys():
				IDmember = hashCluster_detail[j.rstrip()]
				#print IDmember,"IDmember"
				if IDmember !="" and IDmember == maxLabel:
					tp +=1

		totalCluster = hashCluster[maxLabel]

		sumTtC += totalCluster
		fn = totalCluster - tp
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
    
    (options, args) = parser.parse_args()
    if len(sys.argv) != 5:
        parser.error("incorrect number of arguments")
    
    Predicted_File = options.Predicted_clusters_File
    True_file = options.True_clusters_file
    cluster,totalSeq = readResultFile(Predicted_File)
    #print("Cluster : \n\n\n\n\n",cluster,'\n\n\n\n\n\n\n typer cluster : \n\n', type(cluster),'\n\n\ntotalSeq\n\n\n', totalSeq)
    hashCluster , hashCluster_detail = readTrueClusterFile(True_file)
    #print('\n\n\n\nhastCluster : \n\n\n', hashCluster,'\n\n\n\n\n\n\n\nhashcluster_detail\n\n\n\n\n\n\n\n',hashCluster_detail)
    evaluateMeasures(cluster, hashCluster, totalSeq, hashCluster_detail)

#=============================================================================#
if __name__ == "__main__":
    main()
