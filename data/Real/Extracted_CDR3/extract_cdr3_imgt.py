
import sys
#===================================================================================
#Global variables
Input_file = ""


#Usage
usage = "python format_output_realdata.py -i Input_file  \n"

#===================================================================================
#Read parameters
def readParameters(args):
	global Input_file


	for i in range(1,len(args)):
		if (args[i] == "-i"):
			Input_file = args[i+1]
		elif (args[i] == "-h"):
			print usage
#===================================================================================
### Check parameters
def checkParameters():
	if (Input_file == ""):
		print "ERROR::Parameter -i Input_file is required\n"
		sys.exit(1);

#===================================================================================
def read_output_file(filename):
	f=open(filename,"r")
	lines=f.readlines()
	f.close()
	return lines

#===================================================================================
def dico_format(lines):
	Dico_aa={}
	Dico_na={}
	#print lines[0].split("\t")[0],lines[0].split("\t")[-4], lines[0].split("\t")[-5], lines[0].split("\t")[-6], lines[0].split("\t")[-8]
	
	for l in range(1,len(lines)):
		if len(lines[l])< 300 :
			print lines[l],"eknlkndkfn"
		else :
			print len(lines[l])
			if lines[l].split("\t")[-5] == "":
				Dico_aa[l] = lines[l].split("\t")[-4]
			else :
				Dico_aa[l] = lines[l].split("\t")[-5]
			if lines[l].split("\t")[-8] == "":
				Dico_na[l] = lines[l].split("\t")[-6]
			else : 
				Dico_na[l] = lines[l].split("\t")[-8]
	
	return Dico_na, Dico_aa
#===================================================================================

#===================================================================================				
def write_file(dico,file_type):
	outputname=Input_file.split(".")[0]+"_"+file_type+".txt"
	f=open(outputname,"w")
	for key in dico.keys():
		seq_id = ">"+str(key)+"\n"
		f.write(seq_id)
		seq = dico[key]+"\n"
		f.write(seq)
	f.close()
	return 0

#===================================================================================
#			    		Main
#===================================================================================
readParameters(sys.argv)
checkParameters()
lines=read_output_file(Input_file)
Dico_na, Dico_aa= dico_format(lines)
#print Dico_aa
write_file(Dico_aa,"CDR3_AA")
write_file(Dico_na,"CDR3_NA")