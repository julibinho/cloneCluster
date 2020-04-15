# Change-O

Change-O - Repertoire clonal assignment toolkit

/[Change-O - Repertoire clonal assignment toolkit — changeo 0.3.9-2017.10.17 documentation](http://immcantation.readthedocs.io/projects/changeo/en/version-0.3.9---defineclones-brownbag/index.html)/

Change-O is a collection of tools for processing the output of V(D)J alignment tools, assigning clonal clusters to immunoglobulin (Ig) sequences, and reconstructing germline sequences.



For this analysis, We have used the output of IMGT highV/quest 

1-We need to determine an appropriate threshold for trimming the hierarchical clustering into B cell clones (R)

/Determining a clustering threshold/

/Before running DefineClones, it is important to determine an appropriate threshold for trimming the hierarchical clustering into B cell clones. The distToNearest function in the SHazaM R package calculates the distance between each sequence in the data and its nearest neighbor. The resulting distribution is bimodal, with the first mode representing sequences with clonal relatives in the dataset and the second mode representing singletons. The ideal threshold for separating clonal groups is the value that separates the two modes of this distribution and can be found using the findThreshold function in the SHazaM R package/

2-Then run "define clones"(python)