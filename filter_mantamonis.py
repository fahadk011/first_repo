import pandas as pd

# Load dataset (adjust path & extension if different)
df = pd.read_excel("~/Downloads/Mantamonis_bacterial_contamination_analysis.xlsx")

# Select only required columns
filtered = df[["contig ID", "Seq Coverage"]]

# Sort by Seq Coverage in descending order
filtered = filtered.sort_values(by="Seq Coverage", ascending=False)

# Save into your first_repo folder
filtered.to_csv("filtered_mantamonis.csv", index=False)

print("✅ Filtered dataset saved as filtered_mantamonis.csv in first_repo")

