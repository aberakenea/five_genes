import pandas as pd
import os

# Define file paths
sample_map_dir = "/home/abera/data1/data1/five_genes/5genes/uniq_samplemap.tsv"
distance_matrix_dir = "/home/abera/data1/data1/five_genes/distance_matrices"
output_dir = "/home/abera/data1/data1/five_genes/BEB_superpop_results/"
os.makedirs(output_dir, exist_ok=True)  # Create if it doesn't exist

# Genes of interest
genes_of_interest = {"CYP2C9", "PCSK7", "VKORC1", "CNTNAP2", "CYP4F2"}

# Super-populations of interest
super_populations = {"AFR", "SAS", "AMR", "EUR", "EAS"}

# Dictionary to store results
beb_gene_superpop_samples = {gene: {sp: [] for sp in super_populations} for gene in genes_of_interest}

# Cutoff threshold
cutoff = 0.2

# Process each sample map file
for filename in os.listdir(sample_map_dir):
    if not filename.endswith("_uniq_samplemap.tsv"):
        continue  # Skip unrelated files

    # Extract gene name
    gene_name = filename.split("___")[-1].replace("_uniq_samplemap.tsv", "")
    if gene_name not in genes_of_interest:
        continue  # Skip if the gene is not in our list

    # Read the sample map file
    file_path = os.path.join(sample_map_dir, filename)
    df_sample_map = pd.read_csv(file_path, sep="\t", header=None, dtype=str)

    # Dictionary to track BEB sample super-population mapping
    beb_samples_superpop = {}

    # Iterate through sample map to find BEB samples and their super-populations
    for _, row in df_sample_map.iterrows():
        sample_id = row[0]  # Sample name
        populations = row[1:].dropna()  # Population information

        for pop_list in populations:
            pop_list = pop_list.split(",")  # Split multiple populations
            for pop in pop_list:
                pop = pop.strip()
                if "BEB" in pop:  # Find BEB samples
                    for super_pop in super_populations:
                        if super_pop in pop:  # Check if BEB belongs to one of the five super-populations
                            beb_samples_superpop[sample_id] = super_pop
                            break  # Stop checking once super-pop is found

    # Read corresponding distance matrix file
    distance_matrix_file = os.path.join(distance_matrix_dir, f"{gene_name}_distance_matrix.tsv")

    if not os.path.exists(distance_matrix_file):
        print(f"Warning: Distance matrix for {gene_name} not found. Skipping...")
        continue

    df_distance = pd.read_csv(distance_matrix_file, sep="\t", dtype=str)

    # Filter BEB samples based on cutoff
    for _, row in df_distance.iterrows():
        sample_id = row["Sample_ID"]
        score = float(row["Score"])  # Convert score to float

        if sample_id in beb_samples_superpop and score >= cutoff:
            super_pop = beb_samples_superpop[sample_id]  # Get super-population
            beb_gene_superpop_samples[gene_name][super_pop].append(sample_id)

# Print the results
for gene, superpop_samples in beb_gene_superpop_samples.items():
    print(f"\nGene: {gene}")
    for super_pop, samples in superpop_samples.items():
        print(f"  {super_pop}: {len(samples)} BEB samples -> {samples}")
