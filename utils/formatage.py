#! /usr/bin/env python3
# coding: utf-8
def resultat_pour_une_partition(part, i_min):
	res = ''
	for w in set(part.values()) :
			res += "%i" % (i_min + w) + "\t"
			
			
			list_nodes = [nodes for nodes in part.keys() if part[nodes] == w]
			list_nodes.sort()
			for x in list_nodes :
				res += x + "\t"
			res += "\n"
	#print res
	return res

def formatage(dico): #rassemble toutes les partitions
	count = 0
	with open("res.txt", "w" ) as fichier :
		for w in dico.keys() :
			n = len(set(dico[w].values())) 
			fichier.write(resultat_pour_une_partition(dico[w],count))
			count += n
	fichier.close()
	pass 
	

def main():
	formatage({44 : {'S438': 2, 'S439': 2, 'S578': 0, 'S394': 0, 'S430': 1, 'S577': 0, 'S680': 1, 'S441': 2, 'S426': 1, 'S437': 2, 'S40': 1, 'S552': 0, 'S580': 0, 'S581': 0, 'S836': 2, 'S809': 2, 'S302': 2, 'S677': 1, 'S678': 1, 'S679': 1, 'S673': 1, 'S676': 1, 'S282': 2, 'S731': 2, 'S675': 1}, 45 : {'S438': 2, 'S439': 2, 'S578': 0, 'S394': 0, 'S430': 1, 'S577': 0, 'S680': 1, 'S441': 2, 'S426': 1, 'S437': 2, 'S40': 1, 'S552': 0, 'S580': 0, 'S581': 0, 'S836': 2, 'S809': 2, 'S302': 2, 'S677': 1, 'S678': 1, 'S679': 1, 'S673': 1, 'S676': 1, 'S282': 2, 'S731': 2, 'S675': 1}})
	resultat_pour_une_partition({'S438': 2, 'S439': 2, 'S578': 0, 'S394': 0, 'S430': 1, 'S577': 0, 'S680': 1, 'S441': 2, 'S426': 1, 'S437': 2, 'S40': 1, 'S552': 0, 'S580': 0, 'S581': 0, 'S836': 2, 'S809': 2, 'S302': 2, 'S677': 1, 'S678': 1, 'S679': 1, 'S673': 1, 'S676': 1, 'S282': 2, 'S731': 2, 'S675': 1},4)

	


	
if __name__ == "__main__":
	main()
