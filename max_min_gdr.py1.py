import pandas as pd
import json

def find_min_max_gdr(file_path):
    """
    Reads a TSV file, calculates min and max GDR values for each gene and *sub-population*.

    Args:
        file_path (str): The path to the TSV file.

    Returns:
        dict: A dictionary where keys are gene names and values are dictionaries
              containing min/max GDR values, INCLUDING the specific sub-population
              that has those values. Returns an empty dictionary if an error occurs.
    """
    try:
        df = pd.read_csv(file_path, sep='\t')
        genes = df.iloc[:, 0].tolist()
        sub_population_cols = df.columns[1:].tolist()
        result = {}
        for i, gene in enumerate(genes):
            result[gene] = {}
            gene_values = {}
            for col in sub_population_cols:
                try:
                    gdr_value = float(df.iloc[i, df.columns.get_loc(col)])
                    if not pd.isna(gdr_value):
                        gene_values[col] = gdr_value
                except (ValueError, KeyError) as e:
                    print(f"Warning: Could not extract value from column '{col}' for gene '{gene}'. Skipping. Error: {e}")
                    continue

            if not gene_values:
                print(f"Warning: No valid GDR values found for gene '{gene}'. Skipping.")
                result[gene] = {'min': float('NaN'), 'max': float('NaN'), 'min_sub_pop': None, 'max_sub_pop': None}
                continue
            min_sub_pop = min(gene_values, key=gene_values.get)
            min_gdr = gene_values[min_sub_pop]
            max_sub_pop = max(gene_values, key=gene_values.get)
            max_gdr = gene_values[max_sub_pop]
            result[gene] = {
                'min': round(min_gdr, 4),
                'max': round(max_gdr, 4),
                'min_sub_pop': min_sub_pop,
                'max_sub_pop': max_sub_pop
            }

        return result

    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
        return {}
    except pd.errors.EmptyDataError:
        print(f"Error: The file at {file_path} is empty.")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}

file_path = "/home/abera/data1/data1/five_genes/AberaTest__five_genes_distance_matrice_list__Population__gdr.tsv"
output_file = "/home/abera/data1/data1/five_genes/five_genes_gdr_results.json"

result = find_min_max_gdr(file_path)

if result:
    try:
        with open(output_file, "w") as f:
            json.dump(result, f, indent=4)
        print(f"Results saved to {output_file}")
    except IOError as e:
        print(f"Error: Could not write to file {output_file}. Error: {e}")
else:
    print("No results were saved due to errors.")
