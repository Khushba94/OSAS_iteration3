import pandas as pd
from sklearn.cluster import DBSCAN

scaled = pd.read_csv("C:/OSAS/outputs/scaled.csv")

dbscan = DBSCAN(eps=0.4, min_samples=10)
labels = dbscan.fit_predict(scaled)

print("Noise points:", sum(labels == -1))
