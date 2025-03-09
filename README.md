# Excel Sheet for Dataset

This repository provides a complete guide for preparing an Excel sheet from your image dataset. It details every step from renaming images to generating a CSV file with image attributes and converting that CSV file into an Excel sheet.

---

## Table of Contents
- [Prerequisites](#prerequisites)
- [Folder Structure](#folder-structure)
- [Step 1: Renaming Images](#step-1-renaming-images)
- [Step 2: Generating CSV with Attributes](#step-2-generating-csv-with-attributes)
- [Step 3: Converting CSV to Excel](#step-3-converting-csv-to-excel)
- [CSV & Excel Format](#csv--excel-format)
- [Notes](#notes)
- [Conclusion](#conclusion)

---

## Prerequisites

- **Python 3.x**
- **Pandas Library**  
  Install using:
  ```bash
  pip install pandas
  ```

---

## Folder Structure

Ensure your repository follows a similar structure:

```
.
├── animals
│   ├── Cheetah
│   │   ├── cheetah-01.jpg
│   │   └── cheetah-02.jpg
│   ├── Leopard
│   ├── Lion
│   ├── Tiger
│   └── Jaguar
├── rename_images.py
├── generate_csv.py
└── csv_to_excel.py
```

---

## Step 1: Renaming Images

Run the `rename_images.py` script to consistently rename your images for each animal category.

For example, to rename images in the **Cheetah** folder, execute:
```bash
python rename_images.py --folder "animals/Cheetah" --name "cheetah"
```
Repeat the command for other categories (e.g., Lion, Tiger) by updating the folder path and base name.

---

## Step 2: Generating CSV with Attributes

This step creates a CSV file that includes the following columns:
- **Image_Name**
- **Image_Category**
- **Image_Category_No**
- **Attributes:** Speed, Color Pattern, Size, Habitat

The attribute values are encoded as follows:
- **Speed:** 1 = Fast, 0 = Medium, -1 = Slow  
- **Color Pattern:** 1 = Striped, 0 = Spotted, -1 = Plain  
- **Size:** 1 = Large, 0 = Medium, -1 = Small  
- **Habitat:** 1 = Forests, 0 = Grasslands, -1 = Savannah  

Below is an example implementation for `generate_csv.py`:

```python
import os
import pandas as pd

# Define the main folder path where animal category folders are stored
folder_path = "C:/Users/mrabd/Downloads/Compressed/image-processing-toolkit-main/image-processing-toolkit-main/animals/Animals"

# Define categories and their attributes in the format:
# [Category Number, Speed, Color Pattern, Size, Habitat]
animal_attributes = {
    "Cheetah":  [1, 1, 0, -1, 0],
    "Leopard":  [2, 1, 0, 0, 1],
    "Lion":     [3, 0, -1, 1, -1],
    "Tiger":    [4, 0, 1, 1, 1],
    "Jaguar":   [5, 1, 0, 0, 1]
}

data = []
for category, attributes in animal_attributes.items():
    category_no = attributes[0]
    category_path = os.path.join(folder_path, category)
    if os.path.exists(category_path):
        images = sorted([img for img in os.listdir(category_path) if img.endswith((".jpg", ".png", ".jpeg"))])
        for image in images:
            # Append: [Image_Name, Image_Category, Image_Category_No, Speed, Color Pattern, Size, Habitat]
            data.append([image, category, category_no] + attributes[1:])

# Define column names
columns = ["Image_Name", "Image_Category", "Image_Category_No", "Speed", "Color_Pattern", "Size", "Habitat"]

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Create a custom header row for image attributes
header_row = ["", "", "Image Attributes", "Speed", "Color Pattern", "Size", "Habitat"]

# Save DataFrame to CSV without header, then insert the custom header row manually
csv_file = "dataset_with_attributes.csv"
df.to_csv(csv_file, index=False, header=False)

with open(csv_file, "r") as f:
    lines = f.readlines()

lines.insert(0, ",".join(header_row) + "\n")

with open(csv_file, "w") as f:
    f.writelines(lines)

print("CSV file created: dataset_with_attributes.csv")
```

---

## Step 3: Converting CSV to Excel

Convert the generated CSV file into an Excel file by running the `csv_to_excel.py` script. Use the code below:

```python
import pandas as pd

# Update the CSV file path if necessary
csv_file = "dataset_with_attributes.csv"
# Read CSV file; use header=1 so that the second row is treated as the column names
df = pd.read_csv(csv_file, header=1)

excel_file = "dataset_with_attributes.xlsx"
df.to_excel(excel_file, index=False)

print("Excel file created:", excel_file)
```

Execute the script with:
```bash
python csv_to_excel.py
```

---

## CSV & Excel Format

### CSV File Format
The CSV file will have the following structure:
```
,,Image Attributes,Speed,Color Pattern,Size,Habitat
Image_Name,Image_Category,Image_Category_No,Speed,Color_Pattern,Size,Habitat
cheetah-01.jpg,Cheetah,1,1,0,-1,0
lion-01.jpg,Lion,3,0,-1,1,-1
...
```

### Excel File Format
The resulting Excel file will have columns:
| Image_Name     | Image_Category | Image_Category_No | **Image Attributes** | Speed | Color_Pattern | Size | Habitat |
|----------------|----------------|-------------------|----------------------|-------|---------------|------|---------|
| cheetah-01.jpg | Cheetah        | 1                 |                      | 1     | 0             | -1   | 0       |
| lion-01.jpg    | Lion           | 3                 |                      | 0     | -1            | 1    | -1      |

---

## Notes

- **Attribute Values (-1, 0, 1):**
  - **Speed:** 1 (Fast), 0 (Medium), -1 (Slow)
  - **Color Pattern:** 1 (Striped), 0 (Spotted), -1 (Plain)
  - **Size:** 1 (Large), 0 (Medium), -1 (Small)
  - **Habitat:** 1 (Forests), 0 (Grasslands), -1 (Savannah)
