# -*- coding: utf-8 -*-
import os

def tri(data):
	directory = os.path.dirname(__file__) # we get the right path.
	path_to_file = os.path.join(directory, "data/artficial/Extracted_CDR3", data) # with this path, we go inside the folder `data` and get the file.
	#print(path_to_file)
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
	tri('monoclonal_simp_indel_cdr3.fa')
