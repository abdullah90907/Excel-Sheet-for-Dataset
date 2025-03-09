import pandas as pd

# Load the CSV file
csv_file = "files/dataset_with_attributes.csv"
df = pd.read_csv(csv_file)

# Save as Excel (.xlsx)
excel_file = "files/dataset_with_attributes.xlsx"
df.to_excel(excel_file, index=False)

print(f"✅ CSV successfully converted to Excel: {excel_file}")
