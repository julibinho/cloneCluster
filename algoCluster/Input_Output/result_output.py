#! /usr/bin/env python3
# coding: utf-8
def resultat_pour_une_partition(part, i_min):
	res = ''
	for w in set(part.values()) :
			res += "%i" % (i_min + w) + "\t"
			list_nodes = [nodes for nodes in part.keys() if part[nodes] == w]
			list_nodes.sort()
			for x in list_nodes :
				res += x + " "
			res += "\n"
	#print res
	#print(res)
	return res

def generate_output_text(dico, path): #rassemble toutes les partitions
	count = 0
	with open(path, "w" ) as fichier :
		for w in dico.keys() :
			n = len(set(dico[w].values())) 
			fichier.write(resultat_pour_une_partition(dico[w],count))
			count += n
	fichier.close()
	pass 
