import pandas as pd

ncpt = pd.read_csv("C:/OSAS_iteration3/data/ncpt_formatted.csv")
lifestyle = pd.read_csv("C:/OSAS_iteration3/data/mental_health_lifestyle_survey_2024.csv")

print(ncpt.head())
print(lifestyle.head())