import csv
from collections import defaultdict

# Path to the input CSV file
input_file = r'C:\PERT-py\RAW DTP vac coverage 2025-04-03 15-23 UTC.csv'

# Define the range of years for the header (1980 to 2023)
years = list(range(1980, 2024))

# Dictionary to hold coverage data (key: country, value: {year: coverage})
coverage_data = defaultdict(lambda: {year: '' for year in years})

# Read the input CSV file and process the data
with open(input_file, mode='r', newline='', encoding='ISO-8859-1') as infile:
    reader = csv.reader(infile, delimiter=';')
    next(reader)  # Skip header row
    
    # Debug: Check a few rows from the input file
    for row in reader:
        print(row)  # You can remove this after debugging
        
        country, year, coverage = row
        if year.isdigit():
            year = int(year)
            if year in years:
                # Try to convert the coverage to a float, default to '' if empty or invalid
                try:
                    # Check if the coverage is valid
                    coverage_data[country][year] = float(coverage) if coverage else ''
                except ValueError:
                    coverage_data[country][year] = ''  # If coverage is invalid, set to ''

# Output file name
output_file = r'C:\PERT-py\DTP vac coverage 2025-04-03 15-23 UTC.csv'

# Open the CSV file in write mode
with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile, delimiter=';')
    
    # Write the header row: 'Country' followed by the years from 1980 to 2023
    header = ['Country'] + [str(year) for year in years]
    writer.writerow(header)
    
    # Write the rows for each country
    for country, coverage in coverage_data.items():
        row = [country] + [
            f"{coverage.get(year, ''):.2f}" if coverage.get(year, '') != '' else '' for year in years
        ]
        writer.writerow(row)

print(f"CSV file '{output_file}' has been created successfully.")
