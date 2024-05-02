import numpy as np
from sklearn import datasets
from numpy import random

dataset = sklearn.datasets.make_moons(n_samples = 300, noise = 0.3, random_state = 20) # you can change noise and random_state where noise >= 0.15
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.3, random_state = 100)

class KSVM():
