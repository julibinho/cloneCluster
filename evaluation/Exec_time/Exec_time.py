#! /usr/bin/env python3
# coding: utf-8
import argparse
import time
import os
import sys
pwd = os.getcwd()
sys.path.append(pwd+'/algoCluster/Louvain')
sys.path.append(pwd+'/algoCluster/Gclust')
#print(sys.path)


#import LouvainClustering as clustering ##utiliser la fonction exec(path_to_file) pour calculer le temps de calcul sur 
#import gclust as Gclust

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-p","--path_to_file",help="""Chemin vers le fichier à utiliser""")
	parser.add_argument("-a","--algorithm",help="""Chemin vers le fichier à utiliser""")
	return parser.parse_args()


def main():
	args = parse_arguments()
	path_to_file = args.path_to_file
	current_algo=args.algorithm
	if os.environ["ALGO"] == '/home/quentin/Documents/cloneCluster/algoCluster/Gclust/gclust.py':
		import gclust as Gclust
		current_algo = Gclust
	elif os.environ["ALGO"] == '/home/quentin/Documents/cloneCluster/algoCluster/Louvain/LouvainClustering.py':
		import LouvainClustering as clustering
		current_algo = clustering
	start_time = time.time()
	current_algo.execution_time(path_to_file)
	print("Temps d\'execution : %s secondes ---" % (time.time() - start_time))

if __name__ == "__main__": 
	main()












