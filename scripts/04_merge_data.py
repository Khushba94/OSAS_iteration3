import pandas as pd

ncpt = pd.read_csv("C:/OSAS_iteration3/outputs/ncpt_features.csv")
lifestyle = pd.read_csv("C:/OSAS_iteration3/outputs/lifestyle_features.csv")

ncpt["synthetic_id"] = range(len(ncpt))
lifestyle["synthetic_id"] = range(len(lifestyle))

merged = pd.merge(ncpt, lifestyle, on="synthetic_id", how="inner")

merged.to_csv("C:/OSAS_iteration3/outputs/merged.csv", index=False)

print("Merge complete.")