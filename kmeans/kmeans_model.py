import pandas as pd
from sklearn.cluster import KMeans

def train_kmeans():
    data = pd.read_csv("data/kmeans_dataset.csv")

    model = KMeans(n_clusters=3, random_state=42)
    model.fit(data)

    return model, data
