#! /usr/bin/env python3
# coding: utf-8
import os

def reading_csv_from_immuneSIM(path_to_csv, output_path): #cette méthode ne foctionne que pour le formalisme de immuneSIM
    with open(output_path,"w") as fasta_output:
        dico = {}
        first = True
        with open(path_to_csv, "r") as csv_file:
            for line in csv_file:
                if first:
                    first = False
                else :
                    infos = line.split("\" \"")
                    #print(infos)
                    fasta_output.write(">S" + infos[0][1:] + "\n" + infos[1]+"\n")
                    VDJ_combination = infos[4] + infos[5] + infos[6] #dans le fichier csv, cela correspond aux id des gènes v, d et j utilisés. 
                    if VDJ_combination in dico:
                        dico[VDJ_combination].append("S" + infos[0])
                    else :
                        dico[VDJ_combination] = ["S" + infos[0]]
    fasta_output.close()


def main():
    reading_csv_from_immuneSIM("première_sim_avec_immuneSIM.csv", "test_csv_to_fasta.fa")


if __name__ == "__main__":
    main()
