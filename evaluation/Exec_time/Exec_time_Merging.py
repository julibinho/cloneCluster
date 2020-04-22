#! /usr/bin/env python3
# coding: utf-8
import argparse
import time
import os
import sys
pwd = os.getcwd()
sys.path.append(pwd+'/algoCluster/Merging')
#print(sys.path)


import Merging  ##utiliser la fonction exec(path_to_file) pour calculer le temps de calcul sur 

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-c","--cluster_file",help="""résultat de l'algo""")
	parser.add_argument("-d","--data",help="""fasta avec les id et les séquences""")
	return parser.parse_args()

def main():
	args = parse_arguments()
	path_to_file = args.cluster_file
	path_to_data = args.data
	
	start_time = time.time()
	
	Merging.exec(path_to_file, path_to_data)
	
	print("Temps d\'execution : %s secondes ---" % (time.time() - start_time))

if __name__ == "__main__": 
	main()












