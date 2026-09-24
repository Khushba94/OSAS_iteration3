import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

scaled = pd.read_csv("C:/OSAS_iteration3/outputs/scaled.csv")

kmeans = KMeans(n_clusters=4, random_state=42)
labels = kmeans.fit_predict(scaled)

scaled["cluster"] = labels
scaled.to_csv("C:/OSAS_iteration3/outputs/merged_scaled_clustered.csv", index=False)
print("Silhouette:", silhouette_score(scaled, labels))
