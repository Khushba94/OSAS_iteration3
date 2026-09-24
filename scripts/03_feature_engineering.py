import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load cleaned datasets
ncpt = pd.read_csv("C:/OSAS_iteration3/outputs/ncpt_clean.csv")
lifestyle = pd.read_csv("C:/OSAS_iteration3/outputs/mental_health_lifestyle_clean.csv")

# ----------------------------------------------------
# 1. Cognitive Composite Score
# ----------------------------------------------------
ncpt["cognitive_composite_score"] = ncpt[[
    "Attention",
    "MemoryRecall",
    "ProcessingSpeed",
    "Reasoning",
    "WorkingMemory"
]].mean(axis=1)

# ----------------------------------------------------
# 2. Convert categorical lifestyle fields to numeric
# ----------------------------------------------------

exercise_map = {
    "None": 0,
    "1-2x/week": 1,
    "3-5x/week": 2,
    "Daily": 3
}
lifestyle["Exercise_Frequency_Num"] = lifestyle["Exercise_Frequency"].map(exercise_map)

lifestyle["Meditation_Num"] = lifestyle["Meditation_Practice"].map({"Yes": 1, "No": 0})

caffeine_map = {
    "None": 0,
    "1 cup": 1,
    "2-3 cups": 2,
    "4+ cups": 3
}
lifestyle["Caffeine_Num"] = lifestyle["Caffeine_Intake_Daily"].map(caffeine_map)

lifestyle["BMI_Num"] = lifestyle["BMI_Category"].astype("category").cat.codes

# ----------------------------------------------------
# 3. Wellbeing Index (scaled)
# ----------------------------------------------------
scaler = MinMaxScaler()

# Debug: check dtypes
print(lifestyle[[
    "Sleep_Hours_Per_Night",
    "Exercise_Frequency_Num",
    "Self_Reported_Stress_Level",
    "Social_Interactions_Per_Week"
]].dtypes)

lifestyle["wellbeing_index"] = scaler.fit_transform(
    lifestyle[[
        "Sleep_Hours_Per_Night",
        "Exercise_Frequency_Num",
        "Self_Reported_Stress_Level",
        "Social_Interactions_Per_Week"
    ]]
).mean(axis=1)

# ----------------------------------------------------
# 4. Risk Behaviour Score
# ----------------------------------------------------
lifestyle["risk_behaviour_score"] = (
    lifestyle["Daily_Screen_Time_Hours"] +
    lifestyle["Caffeine_Num"] +
    lifestyle["BMI_Num"]
)

# ----------------------------------------------------
# Save engineered datasets
# ----------------------------------------------------
ncpt.to_csv("C:/OSAS_iteration3/outputs/ncpt_features.csv", index=False)
lifestyle.to_csv("C:/OSAS_iteration3/outputs/lifestyle_features.csv", index=False)

print("Feature engineering complete.")
