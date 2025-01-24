import os
import pandas as pd
import re
dist_dir = "/home/abera/data1/data1/distmax_five_genes"

population_mapping = {
    "AFR": "African",
    "EUR": "European",
    "EAS": "East Asian",
    "SAS": "South Asian",
    "AMR": "American"
}
group_description_mapping = {
    "AFR": "Africa",
    "EUR": "Europe",
    "EAS": "East Asia",
    "SAS": "South Asia",
    "AMR": "Americas"
}

all_samples = set()

for filename in os.listdir(dist_dir):
    if filename.endswith(".tsv"):  
        file_path = os.path.join(dist_dir, filename)
        # Read the distance matrix
        df = pd.read_csv(file_path, sep='\t', index_col=0)
        all_samples.update(df.index)

def infer_population(sample_id):
    match = re.match(r"([A-Z]{3})___[A-Z]{3}___", sample_id)  
    if match:
        code = match.group(1)
        return population_mapping.get(code, "Unknown")
    return "Unknown"

def infer_group_name(sample_id):
    match = re.match(r"([A-Z]{3}___[A-Z]{3})___", sample_id) 
    if match:
        return match.group(1)
    return "Unknown"

def infer_group_description(group_name):
    code = group_name.split("___")[0]  
    return group_description_mapping.get(code, "Unknown")

sample_data_rows = []
group_data_dict = {}  

for sample in sorted(all_samples):
    population = infer_population(sample)
    group_name = infer_group_name(sample)
    group_description = infer_group_description(group_name)
    sample_data_rows.append({"SampleID": sample, "Population": population})
    group_data_dict[group_name] = {
        "GroupCategory": "Population",
        "GroupName": group_name,
        "GroupDescription": group_description
    }

sample_data = pd.DataFrame(sample_data_rows)
group_data = pd.DataFrame.from_dict(group_data_dict, orient="index")

sample_data_path = os.path.join(dist_dir, "sample_data.tsv")
group_data_path = os.path.join(dist_dir, "group_data.tsv")

sample_data.to_csv(sample_data_path, sep='\t', index=False)
group_data.to_csv(group_data_path, sep='\t', index=False)

print(f"Files created:\n- {sample_data_path}\n- {group_data_path}")
