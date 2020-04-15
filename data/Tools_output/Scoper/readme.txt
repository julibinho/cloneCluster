For analysing the sequences via Scoper you have to :

1-  Analyse the sequences by IMGT/highVquest annotation

2 - Parse the IMGT/highVquest annotation output via Change-o

		https://changeo.readthedocs.io/en/stable/examples/imgt.html
		command : $ python MakeDb.py imgt -i imgt_output -s fasta_file
		example : $ python MakeDb.py imgt -i mono_simp_indel.txz -s monoclonal_simp_indel.fasta 
3 - Run scoper
