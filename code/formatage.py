#! /usr/bin/env python3
# coding: utf-8

def formatage(dico):
	with open("res.txt", "w" ) as fichier :
		for w in set(dico.values()) :
			fichier.write("%i" % w + " ")
			
			list_nodes = [nodes for nodes in dico.keys() if dico[nodes] == w]
			for x in list_nodes :
				fichier.write(x + " ")
			fichier.write("\n")
	fichier.close()
	pass 
	

def main():
	formatage({'S438': 2, 'S439': 2, 'S578': 0, 'S394': 0, 'S430': 1, 'S577': 0, 'S680': 1, 'S441': 2, 'S426': 1, 'S437': 2, 'S40': 1, 'S552': 0, 'S580': 0, 'S581': 0, 'S836': 2, 'S809': 2, 'S302': 2, 'S677': 1, 'S678': 1, 'S679': 1, 'S673': 1, 'S676': 1, 'S282': 2, 'S731': 2, 'S675': 1})

	


	
if __name__ == "__main__":
	main()
