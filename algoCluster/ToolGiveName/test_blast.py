#! /usr/bin/env python3
# coding: utf-8

from Bio.Blast.Applications import NcbideltablastCommandline




#https://github.com/biopython/biopython/blob/master/Bio/Blast/Applications.py
#http://biopython.org/DIST/docs/api/Bio.Blast.Applications.NcbirpstblastnCommandline-class.html


######https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastSearch&BLAST_SPEC=blast2seq&LINK_LOC=align2seq


from Bio.Blast.Applications import NcbimakeblastdbCommandline
#cline = NcbimakeblastdbCommandline(cmd="ncbi-blast-2.10.0+/bin/makeblastdb",dbtype="nucl",input_file="tool/Archives/test.fa",parse_seqids=True)
#NcbimakeblastdbCommandline(cmd='makeblastdb', dbtype='prot', input_file='NC_005816.faa')
#print(cline)


cline=NcbideltablastCommandline(cmd="ncbi-blast-2.10.0+/bin/deltablast",query="tool/Archives/test.fa",out="opuntia.xml",db='/home/lisa/Programmation/cloneCluster/tool/Archives/test.fa')
print(cline())
#stdout, stderr = cline()

