import os
import pandas as pd

# Define the main folder path
folder_path = "C:/Users/mrabd/Downloads/Compressed/image-processing-toolkit-main/image-processing-toolkit-main/animals/Animals"

# Define categories and their numeric values
animal_attributes = {
    "Cheetah":  [1, 1, 0, -1, 0],  # Fast, Spotted, Small, Grasslands
    "Leopard":  [2, 1, 0, 0, 1],   # Fast, Spotted, Medium, Forests
    "Lion":     [3, 0, -1, 1, -1], # Medium, Plain, Large, Savannah
    "Tiger":    [4, 0, 1, 1, 1],   # Medium, Striped, Large, Forests
    "Jaguar":   [5, 1, 0, 0, 1]    # Fast, Spotted, Medium, Forests
}

# Collect image data
data = []
for category, attributes in animal_attributes.items():
    category_no = attributes[0]  # Extract category number
    category_path = os.path.join(folder_path, category)

    if os.path.exists(category_path):
        images = sorted([img for img in os.listdir(category_path) if img.endswith((".jpg", ".png", ".jpeg"))])
        
        for image in images:
            data.append([image, category, category_no] + attributes[1:])

# Create DataFrame and Save to CSV
columns = ["Image_Name", "Image_Category", "Image_Category_No", "Speed", "Color_Pattern", "Size", "Habitat"]
df = pd.DataFrame(data, columns=columns)
df.to_csv("files/dataset_with_attributes.csv", index=False)

print("✅ CSV file saved successfully in the correct format!")
