import numpy as np
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:100, :2]
y = iris.target[:100]

"""
Make sure you use the method given in the question!
"""