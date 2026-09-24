import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

scaled = pd.read_csv("C:/OSAS/outputs/scaled.csv")

kmeans = KMeans(n_clusters=4, random_state=42)
labels = kmeans.fit_predict(scaled)

print("Silhouette:", silhouette_score(scaled, labels))
