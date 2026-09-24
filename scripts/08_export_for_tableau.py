import pandas as pd

merged = pd.read_csv("C:/OSAS_iteration3/outputs/merged_scaled_clustered.csv")
scaled = pd.read_csv("C:/OSAS_iteration3/outputs/scaled.csv")

final = pd.concat([merged, scaled], axis=1)
final.to_csv("C:/OSAS_iteration3/outputs/merged_for_tableau.csv", index=False)

print("Exported for Tableau.")
