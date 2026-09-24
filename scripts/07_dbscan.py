import pandas as pd
from sklearn.cluster import DBSCAN

scaled = pd.read_csv("C:/OSAS_iteration3/outputs/scaled.csv")

dbscan = DBSCAN(eps=0.4, min_samples=10)
labels = dbscan.fit_predict(scaled)

print("Noise points:", sum(labels == -1))

# params = [(0.3, 5), (0.4, 10), (0.5, 15)]

# for eps, min_samples in params:
#     db = DBSCAN(eps=eps, min_samples=min_samples)
#     labels = db.fit_predict(scaled)
#     noise = list(labels).count(-1)
#     print(f"eps={eps}, min_samples={min_samples}, Noise Points={noise}")
