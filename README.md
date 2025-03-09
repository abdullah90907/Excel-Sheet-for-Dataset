# Excel Sheet for Dataset

This repository provides detailed, step-by-step instructions to prepare an Excel sheet for your image dataset using a series of Python scripts. Follow these steps to organize your dataset from renaming images to converting a CSV file into an Excel file.

## Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Setup Instructions](#setup-instructions)
4. [Steps to Prepare the Excel Sheet](#steps-to-prepare-the-excel-sheet)
5. [Final Output](#final-output)
6. [Contributing](#contributing)
7. [License](#license)

## Overview
This project guides you through creating an Excel sheet that contains:
- **Image Name**
- **Image Category**
- **Image Category Number**
- **Image Attributes** (with sub-headers for Speed, Color Pattern, Size, and Habitat)

The process uses Python scripts to:
- Rename images consistently.
- Generate a CSV file that includes category and attribute information.
- Convert the CSV file to an Excel workbook with an extra header row for the attributes.

## Prerequisites
- **Python 3.x** installed on your computer.
- A text editor or IDE for Python.
- Microsoft Excel or any compatible spreadsheet application.
- Basic understanding of command-line operations.

## Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/excel-sheet-for-dataset.git
   cd excel-sheet-for-dataset
   ```
2. **Set Up a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. **Install Required Packages**
   ```bash
   pip install pandas
   ```

## Steps to Prepare the Excel Sheet

### Step 1: Rename Your Images
- **Purpose:** Ensure that all images in each category folder have consistent, standardized names.
- **What to Run:** Use the provided `rename.py` script.
- **How to Run:**  
  For example, for the "Cheetah" category:
  ```bash
  python rename.py "C:/path/to/your/images/Cheetah" --name cheetah
  ```
- **Repeat:** Run the script for other categories (e.g., Leopard, Lion, Tiger, Jaguar).

### Step 2: Generate the CSV File with Attributes
- **Purpose:** Create a CSV file that lists each image with its corresponding category, category number, and encoded attribute values.
- **What to Run:** Use the CSV generation script (e.g., `generate_csv.py`) provided in the repository.
- **How to Run:**  
  ```bash
  python generate_csv.py
  ```
  - **Note:** This script will scan the categorized image folders, assign the predefined attribute values (using encoding such as -1, 0, 1), and output a file named `dataset_with_attributes.csv`.

### Step 3: Convert the CSV File to Excel Format
- **Purpose:** Transform the CSV file into an Excel file and add an additional header row above the attribute columns labeled "Image Attributes."
- **What to Run:** Use the provided `csv_to_excel.py` script.
- **How to Run:**  
  ```bash
  python csv_to_excel.py
  ```
  - **Result:** This command converts `dataset_with_attributes.csv` into `dataset_with_attributes.xlsx`.

### Step 4: Review the Excel File
- **Purpose:** Ensure that the Excel file has the correct structure and data.
- **What to Do:**
  - Open `dataset_with_attributes.xlsx` in Microsoft Excel or another spreadsheet editor.
  - Verify that the file contains:
    - **Image Name**
    - **Image Category**
    - **Image Category Number**
    - A header row labeled **Image Attributes** above the columns for Speed, Color Pattern, Size, and Habitat.
  - Confirm that all attribute values use the correct encoding (-1, 0, 1).

## Final Output
After completing the above steps, your final Excel file (`dataset_with_attributes.xlsx`) will include:
- **Image Name:** The filename of each image.
- **Image Category:** The category (e.g., Cheetah, Lion, etc.).
- **Image Category Number:** A unique number representing each category.
- **Image Attributes:** A section header with subsequent columns for:
  - **Speed**
  - **Color Pattern**
  - **Size**
  - **Habitat**

## Contributing
Contributions are welcome! Fork the repository, create a new branch for your improvements, and submit a pull request with your changes.

## License
This project is licensed under the MIT License.
```
