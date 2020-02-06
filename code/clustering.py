#! /usr/bin/env python3
# coding: utf-8
import argparse
import tri_des_seq as tri

def parse_arguments():
    parser = argparse.ArgumentParser()
    #parser.add_argument("-e", "--extension", help="""Quelle extension a le fichier ?""")
    parser.add_argument("-d","--datafile",help="""Quel fichier Fasta souhaite-t-on analyser ?""")
    return parser.parse_args()

def main():
	args = parse_arguments()
	datafile = args.datafile
	Dico_des_sequences = tri.tri(datafile)
	
if __name__ == "__main__": # Sert à executer tout le corp de la fonction main, définie juste au dessus, quand on lance l'execution.
	main()
