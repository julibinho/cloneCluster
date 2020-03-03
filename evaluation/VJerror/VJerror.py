import sys
from collections import Counter
from optparse import OptionParser
#===================================================================================
def read_output_file(filename):
	f=open(filename,"r")
	lines=f.readlines()
	f.close()
	return lines
#===================================================================================
def dico_VJ_format(lines):
	dico_VJ={}
	for l in range(0,len(lines)):
		split=lines[l].split("\t")
		dico_VJ[split[0]]=[split[1],split[2]]
	return dico_VJ
#===================================================================================
def creat_dico_cluster_VJ (dico_VJ ,cluster_lines) :
	dico_cluster_VJ = {}
	for l in range(0,len(cluster_lines)):
		split=cluster_lines[l].split("\t")
		dico_cluster_VJ[split[0]] = [[],[]] # V list and J list 
		for seq in split[1].split(" ") :
			dico_cluster_VJ[split[0]][0].append(dico_VJ[seq.rstrip()][0].rstrip())
			dico_cluster_VJ[split[0]][1].append(dico_VJ[seq.rstrip()][1].rstrip())
	return dico_cluster_VJ


def calculate_error(dico_cluster_VJ):
	listloc=[]
	for key in dico_cluster_VJ.keys():
		if len(set(dico_cluster_VJ[key][0])) != 1:
			dico_V=dict( Counter(dico_cluster_VJ[key][0]))
			maximum = max(dico_V, key=dico_V.get)
			final_V=(sum(dico_V.values())-dico_V[maximum])/float(sum(dico_V.values()))
			listloc.append( final_V)
			dico_J=dict( Counter(dico_cluster_VJ[key][1]))
			maximum = max(dico_J, key=dico_J.get)
			final_J=(sum(dico_J.values())-dico_J[maximum])/float(sum(dico_J.values()))
			listloc.append( final_J)
		else:
			listloc.append(1)
			listloc.append(1)
	print("The VJ error is : ", 1-(sum(listloc) / float(len(listloc))))
	return 1-(sum(listloc) / float(len(listloc)))


#===================================================================================
def main():
	usage = "python  VJerror.py -a < formated annotation file > -t <tool formated output>\n "
	parser = OptionParser(usage)
	parser.add_option("-a", "--formated_annotation_file", dest="formated_annotation_file",
		  help="V and J of each sequence, anootated by IMGT")
	parser.add_option("-t", "--tool_formated_output", dest="tool_formated_output",
		help="formated output of each clustering tool")
	
	(options, args) = parser.parse_args()
	if len(sys.argv) != 5:
		parser.error("incorrect number of arguments")

	VJ_file = options.formated_annotation_file
	tool_output = options.tool_formated_output
	VJ_lines = read_output_file(VJ_file)
	VJ_dico = dico_VJ_format(VJ_lines)
	cluster_lines = read_output_file(tool_output)
	dico_cluster_VJ = creat_dico_cluster_VJ (VJ_dico, cluster_lines)
	calculate_error(dico_cluster_VJ)

#=============================================================================#
if __name__ == "__main__":
	main()
