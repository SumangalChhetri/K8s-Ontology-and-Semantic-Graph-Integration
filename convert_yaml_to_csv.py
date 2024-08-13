import yaml
import csv

# Load the YAML file
with open('relationships.yaml', 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)

# Define the CSV file
with open('relationships.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    # Write the header based on your YAML structure
    writer.writerow(['deployment', 'pod'])

    # Write the data
    for item in data:
        writer.writerow([item['deployment'], item['pod']])
