import numpy as np
from sklearn import datasets
from numpy import random
iris=datasets.load_iris()
x=iris.data[50:,[2,3]]
y=iris.target[50:]

