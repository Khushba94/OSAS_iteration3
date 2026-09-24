import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

merged = pd.read_csv("C:/OSAS_iteration3/outputs/merged.csv")

# Correct feature list
features = [
    "Attention",
    "MemoryRecall",
    "ProcessingSpeed",
    "Reasoning",
    "WorkingMemory",
    "cognitive_composite_score",
    "Daily_Screen_Time_Hours",
    "Sleep_Hours_Per_Night",
    "Exercise_Frequency_Num",
    "Self_Reported_Stress_Level",
    "Social_Interactions_Per_Week",
    "wellbeing_index",
    "risk_behaviour_score"
]

# Remove rows with ANY missing values in these columns
merged = merged.dropna(subset=features)

# Scale numeric features
scaler = StandardScaler()
scaled_data = scaler.fit_transform(merged[features])

scaled_df = pd.DataFrame(scaled_data, columns=features)

scaled_df.to_csv("C:/OSAS_iteration3/outputs/scaled.csv", index=False)

print("Scaling complete.")
