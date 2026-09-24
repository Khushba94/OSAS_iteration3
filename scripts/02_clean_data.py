import pandas as pd
import numpy as np

# Load data
ncpt = pd.read_csv("C:/OSAS/data/ncpt_formatted.csv")
lifestyle = pd.read_csv("C:/OSAS/data/mental_health_lifestyle_survey_2024.csv")

# Convert numeric-looking strings to numbers
numeric_cols = [
    "Attention",
    "MemoryRecall",
    "ProcessingSpeed",
    "Reasoning",
    "WorkingMemory",
    "grand_index",
    "education_level",
    "age_band_derive",
    "time_of_day"
]

for col in numeric_cols:
    ncpt[col] = pd.to_numeric(ncpt[col], errors="coerce")

# Fill missing numeric values
ncpt = ncpt.fillna(ncpt.median(numeric_only=True))

# Winsorise outliers for cognitive scores
for col in numeric_cols:
    col_data = ncpt[col]
    ncpt[col] = np.where(
        col_data > col_data.mean() + 3 * col_data.std(),
        col_data.mean() + 3 * col_data.std(),
        col_data
    )

# Lifestyle cleaning
lifestyle["Sleep_Hours_Per_Night"] = lifestyle["Sleep_Hours_Per_Night"].fillna(
    lifestyle["Sleep_Hours_Per_Night"].median()
)
lifestyle["Self_Reported_Stress_Level"] = lifestyle["Self_Reported_Stress_Level"].fillna(
    lifestyle["Self_Reported_Stress_Level"].mode()[0]
)
lifestyle["Daily_Screen_Time_Hours"] = lifestyle["Daily_Screen_Time_Hours"].clip(upper=15)

# Save cleaned files
ncpt.to_csv("C:/OSAS/outputs/ncpt_clean.csv", index=False)
lifestyle.to_csv("C:/OSAS/outputs/mental_health_lifestyle_clean.csv", index=False)

print("Cleaning complete.")