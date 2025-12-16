import pandas as pd
from knn_model import train_knn

model, le = train_knn()

# New person (use DataFrame to match training format)
new_person = pd.DataFrame([[168, 60]], columns=["Height", "Weight"])

prediction = model.predict(new_person)

print("Predicted Gender:", le.inverse_transform(prediction)[0])
