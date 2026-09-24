import pandas as pd

merged = pd.read_csv("C:/OSAS/outputs/merged.csv")
scaled = pd.read_csv("C:/OSAS/outputs/scaled.csv")

final = pd.concat([merged, scaled], axis=1)
final.to_csv("C:/OSAS/outputs/merged_for_tableau.csv", index=False)

print("Exported for Tableau.")
