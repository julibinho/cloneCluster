#! /usr/bin/env python3
# coding: utf-8
import argparse
import time
import os
import sys
pwd = os.getcwd()
sys.path.append(pwd+'/algoCluster/Louvain')
#print(sys.path)


import LouvainClustering as clustering ##utiliser la fonction exec(path_to_file) pour calculer le temps de calcul sur 

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-p","--path_to_file",help="""Chemin vers le fichier à utiliser""")
	return parser.parse_args()


def main():
	args = parse_arguments()
	path_to_file = args.path_to_file
	start_time = time.time()
	clustering.exec(path_to_file)
	print("Temps d\'execution : %s secondes ---" % (time.time() - start_time))

if __name__ == "__main__": 
	main()












