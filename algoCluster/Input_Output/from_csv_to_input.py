#! /usr/bin/env python3
# coding: utf-8
import os

def reading_csv_from_immuneSIM(path_to_csv, output_fasta_path, output_true_c_path): #cette méthode ne foctionne que pour le formalisme de immuneSIM
    with open(output_fasta_path,"w") as fasta_output:
        dico = {}
        first = True
        with open(path_to_csv, "r") as csv_file:
            for line in csv_file:
                if first:
                    first = False
                else :
                    infos = line.split("\" \"")
                    #print(infos)
                    name = "S"+  infos[0][1:]
                    fasta_output.write(">" + name + "\n" + infos[1]+"\n")
                    VDJ_combination = infos[5] + infos[6] + infos[7] #dans le fichier csv, cela correspond aux id des gènes v, d et j utilisés. 
                    if VDJ_combination in dico:
                        dico[VDJ_combination].append(name)
                    else :
                        dico[VDJ_combination] = [name]
    print(dico)
    make_true_cluster(output_true_c_path,dico)
    fasta_output.close()

def make_true_cluster(true_cluster_path, dico):
    with open(true_cluster_path,"w") as output:
        count = 1
        for w in dico.keys():
            output.write(str(count) + "\t")
            for s in dico[w]:
                output.write(s + " ")
            output.write("\n")
    output.close()

def main():
    reading_csv_from_immuneSIM("essai_csv.csv", "test_csv_fasta.fa", "test_true_cluster.txt")


if __name__ == "__main__":
    main()
