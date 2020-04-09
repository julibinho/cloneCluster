library("scoper")

setwd('/Users/nikaabdollahi/Desktop/Simulated/Raw_output/Scoper/Chage-o_output')
dat<- read.table("l0046_poly_db-pass.tab",sep="\t", header=TRUE,stringsAsFactors=FALSE)

dat[,4] = toupper(dat[,4]) # Junction sequences should be in uppercase

# clone data using defineClonesScope function
ptm <- proc.time()
dataset <- defineClonesScoper(dat, junction = "JUNCTION", v_call = "V_CALL",j_call = "J_CALL", first = TRUE)
proc.time() - ptm

export <- dataset[,c("CLONE","SEQUENCE_ID","JUNCTION")]
write.table(export, file = "l0046_poly_scoper.txt", quote = FALSE, sep = "\t", row.names = FALSE,
            col.names = FALSE)

