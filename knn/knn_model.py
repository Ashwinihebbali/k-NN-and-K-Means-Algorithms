import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

def train_knn():
    data = pd.read_csv("data/knn_dataset.csv")

    X = data[['Height', 'Weight']]
    y = data['Gender']

    le = LabelEncoder()
    y = le.fit_transform(y)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X, y)

    return model, le
