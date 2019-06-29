import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs

X, y = make_blobs(n_samples=100, centers=1, n_features=2, random_state=0)

plt.scatter(*zip(*X), marker = '.', color = 'black')
plt.show()
