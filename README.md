Here is the required information to calculate the GDR_values of five genes, then here is what I did sequencially:
A fter downloading the five genes with their distance matrix I was run the python code(five_genes.tsv.py) to generate both sample_data.tsv and group_data.tsv.
Preparing the file that contain "distance matrix file path", and adjusting my yaml file(willowj_calcGDR_v5.yaml).
finally running the willowj: java -jar -Dlog4j.configurationFile=file:"/home/abera/data1/data1/five_genes/willowTestData/gdr.log4j2.xml" WillowJ.jar -c "/home/abera/data1/data1/five_genes/willowTestData/willowj_calcGDR_v5.yaml"
After running it I  got the result only for one gene (i.e., ENSG00000138109___CYP2C9__dist_max.tsv) even there is no any value for as a result shows in this file " 
# Based on these information how I can over the error and try to get the exact results for all five genes?
