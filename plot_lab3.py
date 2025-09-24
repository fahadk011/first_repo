import pandas as pd
import matplotlib.pyplot as plt

filename = "Mantamonis_bacterial_contamination_analysis.xlsx"


df = pd.read_excel(filename)

counts = df["Preliminary Verdict:"].value_counts()

plt.figure(figsize=(8, 5))
counts.plot(kind="bar")
plt.title("Counts by Preliminary Verdict")
plt.xlabel("Preliminary Verdict")
plt.ylabel("Count")
plt.tight_layout()

plt.savefig("preliminary_classification.png", dpi=200)
print("Saved figure -> preliminary_classification.png")

