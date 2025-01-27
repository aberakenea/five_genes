Here is the required information to calculate the GDR_values of five genes, then, here is what I did sequencially:
A fter downloading the five genes with their distance matrix I was run the python code(five_genes.tsv.py) to generate both sample_data.tsv and group_data.tsv.
Preparing the file that contain "distance matrix file path", and adjusting my yaml file(willowj_calcGDR_v5.yaml).
finally running the willowj: java -jar -Dlog4j.configurationFile=file:"/home/abera/data1/data1/five_genes/willowTestData/gdr.log4j2.xml" WillowJ.jar -c "/home/abera/data1/data1/five_genes/willowTestData/willowj_calcGDR_v5.yaml"
After running it Only one gene's results were produced(i.e., ENSG00000138109___CYP2C9__dist_max.tsv) and the output file " AberaTest_GDR_Calculation__five_genes_distmats_list__Population__gdr.tsv" was empiity.
# Based on these information how I can over come the error and get the exact results for all five genes?

I have used the "distance_matrices" you send me through dropbox, both new_sample_data.tsv and group_data.tsv that I was used for one gene last 7 months ago, yaml file is "willowj_calcGDR_v5.yaml".
And I have adjusted the required information for willowj.
Then ruuning willowj command here: abera@AberaSam:~/data1/data1/five_genes/willowTestData$ java -jar -Dlog4j.configurationFile=file:"/home/abera/data1/data1/five_genes/willowTestData/gdr.log4j2.xml" WillowJ.jar -c "/home/abera/data1/data1/five_genes/willowTestData/willowj_calcGDR_v5.yaml"
# After finishing willowj I get the error that willowj does not calculated the GDR_value for "ENSG00000174469___CNTNAP2__dist_max.tsv.gz" at line number 44 below and the error says "ava.lang.ArrayIndexOutOfBoundsException: Index -1 out of bounds for length 10" at line number 45 below.
Hre is the command I run: abera@AberaSam:~/data1/data1/five_genes/willowTestData$ java -jar -Dlog4j.configurationFile=file:"/home/abera/data1/data1/five_genes/willowTestData/gdr.log4j2.xml" WillowJ.jar -c "/home/abera/data1/data1/five_genes/willowTestData/willowj_calcGDR_v5.yaml"
10:18:44.774 [main] INFO   - initializing
10:18:44.789 [main] INFO   - parse arguments
10:18:44.811 [main] INFO   - YAML configuration file is </home/abera/data1/data1/five_genes/willowTestData/willowj_calcGDR_v5.yaml>
10:18:45.331 [main] INFO  willow.GDRCalculator - ------loading YAML file </home/abera/data1/data1/five_genes/willowTestData/willowj_calcGDR_v5.yaml>
10:18:45.695 [main] INFO  willow.GDRCalculator - willow.WillowParams@764faa6[
  analysis_name=AberaTest_GDR_Calculation
  distance_matrix_filelist=/home/abera/data1/data1/five_genes/willowTestData/five_genes_distance_matrice_list.txt
  func=calcGDR
  group_category_definitions_file=/home/abera/data1/data1/five_genes/willowTestData/group_data.tsv
  num_random_values=0
  output_folder=/home/abera/data1/data1/five_genes/willowTestData/GDRcalculationResultSJ
  output_unprocessed=GDRcalculation_unprocessed_samplesJ.tsv
  sample_group_info_file=/home/abera/data1/data1/five_genes/willowTestData/new_sample_data.tsv
]
10:18:45.699 [main] INFO  willow.GDRCalculator - ------done </home/abera/data1/data1/five_genes/willowTestData/willowj_calcGDR_v5.yaml>
10:18:45.719 [main] INFO  willow.GDRCalculator - ------read <1> categories
10:18:45.725 [main] INFO  willow.GDRCalculator - ------population:	AFR___GWD	AFR___ACB	AFR___GWD	AFR___LWK	SAS___BEB	AFR___ACB	AMR___PUR	EAS___CDX	EAS___KHV	EAS___CHS
10:18:45.744 [main] INFO  willow.GDRCalculator - ------found <1> categories
10:18:45.750 [main] INFO  willow.GDRCalculator - ------read <10> sample entries
10:18:45.752 [main] INFO  willow.GDRCalculator - ------done 
10:18:45.800 [main] INFO  willow.GDRCalculator - ------load distance matrix filelist from file <null>
10:18:45.838 [main] INFO  willow.GDRCalculator - ------found a total of <5> distance matrices
10:18:45.875 [main] INFO  willow.GDRCalculator - sorted
10:18:45.877 [main] INFO  willow.GDRCalculator - ------prepareOutputFoldersForCDRGDR
10:18:46.000 [main] INFO  willow.GDRCalculator - ------finished
10:18:46.003 [main] INFO  willow.GDRCalculator - ------/home/abera/data1/data1/five_genes/willowTestData/distance_matrices/ENSG00000138109___CYP2C9__dist_max.tsv.gz
10:18:46.590 [main] INFO  willow.GDRCalculator - ------total load time for dist matrix is 0s
10:18:46.594 [main] INFO  willow.GDRCalculator - ------total time for fasterCalcCDRGDR is 0ms
10:18:46.654 [main] INFO  willow.GDRCalculator - ------/home/abera/data1/data1/five_genes/willowTestData/distance_matrices/ENSG00000167397___VKORC1__dist_max.tsv.gz
10:18:46.714 [main] INFO  willow.GDRCalculator - ------total load time for dist matrix is 0s
10:18:46.715 [main] INFO  willow.GDRCalculator - ------total time for fasterCalcCDRGDR is 0ms
10:18:46.718 [main] INFO  willow.GDRCalculator - ------/home/abera/data1/data1/five_genes/willowTestData/distance_matrices/ENSG00000174469___CNTNAP2__dist_max.tsv.gz
java.lang.ArrayIndexOutOfBoundsException: Index -1 out of bounds for length 10
	at willow.GDRCalculator.loadDistanceMatrix(GDRCalculator.java:455)
	at willow.GDRCalculator.calcGDRsInList(GDRCalculator.java:670)
	at willow.GDRCalculator.executeGDRCommand(GDRCalculator.java:199)
	at willow.WillowJ.main(WillowJ.java:30)

