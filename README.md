I have used the "distance_matrices" you send me through dropbox, both new_sample_data.tsv and group_data.tsv that I was used for one gene last 7 months ago, yaml file is "willowj_calcGDR_v5.yaml".
And I have adjusted the required information for willowj.
Then ruuning willowj command here: abera@AberaSam:~/data1/data1/five_genes/willowTestData$ java -jar -Dlog4j.configurationFile=file:"/home/abera/data1/data1/five_genes/willowTestData/gdr.log4j2.xml" WillowJ.jar -c "/home/abera/data1/data1/five_genes/willowTestData/willowj_calcGDR_v5.yaml"
# After finishing willowj I get the error that willowj does not calculated the GDR_value for "ENSG00000174469___CNTNAP2__dist_max.tsv.gz" at line number 37 below and the error says "ava.lang.ArrayIndexOutOfBoundsException: Index -1 out of bounds for length 10" at line number 38 below.
abera@AberaSam:~/data1/data1/five_genes/willowTestData$ java -jar -Dlog4j.configurationFile=file:"/home/abera/data1/data1/five_genes/willowTestData/gdr.log4j2.xml" WillowJ.jar -c "/home/abera/data1/data1/five_genes/willowTestData/willowj_calcGDR_v5.yaml"
11:21:16.616 [main] INFO   - initializing
11:21:16.633 [main] INFO   - parse arguments
11:21:16.655 [main] INFO   - YAML configuration file is </home/abera/data1/data1/five_genes/willowTestData/willowj_calcGDR_v5.yaml>
11:21:17.189 [main] INFO  willow.GDRCalculator - ------loading YAML file </home/abera/data1/data1/five_genes/willowTestData/willowj_calcGDR_v5.yaml>
11:21:17.561 [main] INFO  willow.GDRCalculator - willow.WillowParams@764faa6[
  analysis_name=AberaTest_GDR_Calculation
  distance_matrix_filelist=/home/abera/data1/data1/five_genes/willowTestData/five_genes_distance_matrice_list.txt
  func=calcGDR
  group_category_definitions_file=/home/abera/data1/data1/five_genes/willowTestData/group_data.tsv
  num_random_values=0
  output_folder=/home/abera/data1/data1/five_genes/willowTestData/GDRcalculationResultSJ
  output_unprocessed=GDRcalculation_unprocessed_samplesJ.tsv
  sample_group_info_file=/home/abera/data1/data1/five_genes/willowTestData/new_sample_data.tsv
]
11:21:17.565 [main] INFO  willow.GDRCalculator - ------done </home/abera/data1/data1/five_genes/willowTestData/willowj_calcGDR_v5.yaml>
11:21:17.587 [main] INFO  willow.GDRCalculator - ------read <1> categories
11:21:17.592 [main] INFO  willow.GDRCalculator - ------population:	AFR___GWD	AFR___ACB	AFR___GWD	AFR___LWK	SAS___BEB	AFR___ACB	AMR___PUR	EAS___CDX	EAS___KHV	EAS___CHS
11:21:17.612 [main] INFO  willow.GDRCalculator - ------found <1> categories
11:21:17.618 [main] INFO  willow.GDRCalculator - ------read <10> sample entries
11:21:17.619 [main] INFO  willow.GDRCalculator - ------done 
11:21:17.668 [main] INFO  willow.GDRCalculator - ------load distance matrix filelist from file <null>
11:21:17.704 [main] INFO  willow.GDRCalculator - ------found a total of <5> distance matrices
11:21:17.750 [main] INFO  willow.GDRCalculator - sorted
11:21:17.751 [main] INFO  willow.GDRCalculator - ------prepareOutputFoldersForCDRGDR
11:21:17.887 [main] INFO  willow.GDRCalculator - ------finished
11:21:17.890 [main] INFO  willow.GDRCalculator - ------/home/abera/data1/data1/five_genes/willowTestData/distance_matrices/ENSG00000138109___CYP2C9__dist_max.tsv.gz
11:21:18.498 [main] INFO  willow.GDRCalculator - ------total load time for dist matrix is 0s
11:21:18.502 [main] INFO  willow.GDRCalculator - ------total time for fasterCalcCDRGDR is 0ms
11:21:18.572 [main] INFO  willow.GDRCalculator - ------/home/abera/data1/data1/five_genes/willowTestData/distance_matrices/ENSG00000167397___VKORC1__dist_max.tsv.gz
11:21:18.732 [main] INFO  willow.GDRCalculator - ------total load time for dist matrix is 0s
11:21:18.733 [main] INFO  willow.GDRCalculator - ------total time for fasterCalcCDRGDR is 0ms
11:21:18.737 [main] INFO  willow.GDRCalculator - ------/home/abera/data1/data1/five_genes/willowTestData/distance_matrices/ENSG00000174469___CNTNAP2__dist_max.tsv.gz
java.lang.ArrayIndexOutOfBoundsException: Index -1 out of bounds for length 10
	at willow.GDRCalculator.loadDistanceMatrix(GDRCalculator.java:455)
	at willow.GDRCalculator.calcGDRsInList(GDRCalculator.java:670)
	at willow.GDRCalculator.executeGDRCommand(GDRCalculator.java:199)
	at willow.WillowJ.main(WillowJ.java:30)

