import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

scaled = pd.read_csv("C:/OSAS_iteration3/outputs/scaled.csv")
corr = scaled.corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=False, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()