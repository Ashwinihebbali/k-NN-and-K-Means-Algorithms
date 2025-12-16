from kmeans_model import train_kmeans

model, data = train_kmeans()

labels = model.predict(data)

print("Cluster Labels:")
print(labels)
