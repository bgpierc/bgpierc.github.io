import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from scipy.spatial import ConvexHull
from alpha_shape import ConcaveHull

X, y = make_blobs(n_samples=100, centers=1, n_features=2, random_state=0)

hull = ConvexHull(X)

for simplex in hull.simplices:
    plt.plot(X[simplex, 0], X[simplex, 1], 'k-', color = 'red')

plt.scatter(*zip(*X), marker = '.', color = 'black')
#plt.show()

hull = ConcaveHull(X).calc_hull()
print(type(hull))
plt.plot(*hull.exterior.xy)
plt.show()
