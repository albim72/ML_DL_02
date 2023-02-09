# -*- coding: utf-8 -*-

# -- Sheet --

import time
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from sklearn.ensemble import RandomForestClassifier

n_jobs = -1

data = fetch_olivetti_faces()
X,y = data.data, data.target

mask = y<5
X=X[mask]
y=y[mask]

forest = RandomForestClassifier(n_estimators=750,n_jobs=n_jobs, random_state=42)
forest.fit(X,y)

starttime = time.perf_counter()
img_shape = data.images[0].shape
importances = forest.feature_importances_
elapsed_time = time.perf_counter()

print(f"czas wykonania analizy: {elapsed_time-starttime:.3f} s")
img_reshaped = importances.reshape(img_shape)
plt.matshow(img_reshaped,cmap=plt.cm.hot)
plt.title("piksele istotne w ludzkiej twarzy")
plt.colorbar()
plt.show()

