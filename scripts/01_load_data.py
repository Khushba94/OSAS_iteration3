import pandas as pd

ncpt = pd.read_csv("C:/OSAS/data/ncpt_formatted.csv")
lifestyle = pd.read_csv("C:/OSAS/data/mental_health_lifestyle_survey_2024.csv")

print(ncpt.head())
print(lifestyle.head())