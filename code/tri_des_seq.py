# -*- coding: utf-8 -*-


def tri(path_to_file):
	dico = {}
	with open(path_to_file, "r") as fasta_file:
		for line in fasta_file:
			if not line.startswith(">"):
				s = line.strip()
				#Set.append()
				if len(s) not in dico :
					dico[len(s)] = [s]
				else :
					dico[len(s)].append(s)
	#print dico
	return dico

def main():
	pass
	
if __name__ == "__main__":
	tri('data/artficial/Extracted_CDR3/monoclonal_simp_indel_cdr3.fa')
