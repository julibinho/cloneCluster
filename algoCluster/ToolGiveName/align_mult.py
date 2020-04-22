#! /usr/bin/env python3
# coding: utf-8
import os
from Bio.Blast.Applications import NcbideltablastCommandline
from Bio.Blast.Applications import NcbimakeblastdbCommandline
alphabet = ['A','C','G','T']


#https://github.com/biopython/biopython/blob/master/Bio/Blast/Applications.py
#http://biopython.org/DIST/docs/api/Bio.Blast.Applications.NcbirpstblastnCommandline-class.html


######https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastSearch&BLAST_SPEC=blast2seq&LINK_LOC=align2seq


def cmd_blast(nom_db, nom_input, nom_query, nom_output):
    cline = NcbimakeblastdbCommandline(cmd="makeblastdb", dbtype="nucl",input_file= nom_input, out = nom_db,parse_seqids=True)
    txt = cline()
    i = txt[0].find('added ')
    j = txt[0].find('sequences', i)
    nb_seq= int(txt[0][i+6:j])
    
    cline=NcbideltablastCommandline(cmd="blastn", query= nom_query , out= nom_output,db=nom_db, outfmt = 3, evalue = 0.001, max_target_seqs = 20)
    cline()
    return nb_seq

def length_max_seqs(nom_input):
    length = 0
    with open(nom_input, "r") as fasta:
        for line in fasta:
            if not line.startswith('>'):
                if len(line) > length:
                    length = len(line)

    length = length -1
    return length
    
def read_alignment(nom_output, length):
    align = [[0]*4 for i in range(length)]
    with open(nom_output, "r") as blast_out:
        here = False
        ref = ''
        count = 0 
        for line in blast_out:
            if line.startswith('Length=' + str(length)):
                here = True 
            if here and line.startswith('Query'):
                line_ref = line.strip().split()
                ref += line_ref[2]
            if here and line.startswith('S') and ref != '':
                line_seq = line.strip().split()
                seq = line_seq[2]
                shift = int(line_seq[1]) -1
                for i in range(len(seq)):
                    if seq[i] == '.':
                        align[i+ shift][alphabet.index(ref[i])] +=1
                    else :  
                        align[i+ shift][alphabet.index(seq[i])] +=1
            
        
        
            if here and line.startswith('Lambda'):
                here = False
            
                break
    return normalise(align)


def align_mult(nom_input):
    nom_db = "db"+nom_input
    nom_output = "output" + nom_input
    nb_seq = cmd_blast(nom_db, nom_input, nom_input, nom_output)
    res = read_alignment(nom_output, length_max_seqs(nom_input))
    cmd = 'rm ' + nom_db + '.nhr ' + nom_db + '.nog ' + nom_db + '.nsi ' + nom_db + '.nin ' + nom_db + '.nsd ' + nom_db + '.nsq ' + nom_output
    os.system(cmd) # permet de supprimer tous les fichiers crées lors de la création de la base de donnée blast. 
    return res  


def read_score(nom_output):
    with open(nom_output, "r") as blast_out:
        here = False
        for line in blast_out:
            if line.startswith('Sequences producing significant alignments'):
                here = True
            elif here and line.startswith('S'):
                al= line.strip().split()
                #print('al')
                return al[1]
    #print('\n\n\n\n\nl\'alignement n\'a pas marché')
    #with open(nom_output, "r") as blast_out:
    #    for line in blast_out:
    #        print(line)
    #print('\n\n\n\n\n\n')
    return 0
 
def dist_blast(nom_input, nom_query):
    nom_db = "db"+nom_input
    nom_output = "output" + nom_input
    nb_seq = cmd_blast(nom_db, nom_input, nom_query, nom_output)
    #print('nb seq dans dist_blast : ', nb_seq)
    res = read_score(nom_output)
    cmd = 'rm ' + nom_db + '.nhr ' + nom_db + '.nog ' + nom_db + '.nsi ' + nom_db + '.nin ' + nom_db + '.nsd ' + nom_db + '.nsq ' + nom_output
    os.system(cmd) # permet de supprimer tous les fichiers crées lors de la création de la base de donnée blast. 
    return res  
    
def normalise(align):
    for i in range(len(align)):
        s = align[i][0] + align[i][1] + align[i][2] + align[i][3]
        if align[i][0] != 0:
            align[i][0] = align[i][0]/s
        if align[i][1] != 0:
            align[i][1] = align[i][1]/s
        if align[i][2] != 0:
            align[i][2] = align[i][2]/s
        if align[i][3] != 0:
            align[i][3] = align[i][3]/s
    return align


def main():
    nom_input = 'fasta1.fa'
    res = align_mult(nom_input)
    print('res', res)
    
    
if __name__ == "__main__": 
	main()
