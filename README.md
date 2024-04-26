# Coding-Assignment

## Introduction

This assignment focuses on understanding and applying the concepts of soft and hard margins, kernel tricks, and optimization methods in Support Vector Machines (SVM). By solving the given problems and compiling a report, you will demonstrate your grasp of these important machine learning techniques.  

## Deadline
May 12, 2024 11:59PM KST (One day delay is permitted with linear scale score deduction. (20% per day))

### Submission checklist
* Push your code to Git
* Submit your report to LMS

## Files
Files you will edit:
* `SVM_hard.py` : You need to modify this file to implement SVM with hard margin.
* `SVM_soft.py` : You need to modify this file to implement SVM with soft margin.
* `kernel.py` : You need to modify this file to implement kernels which will be used to soft margin.
* `utils.py` : A bunch of utility functions!
* `test.py` : A testing code! I will run this code to run your models.

## What to submit

### Note
**Academic dishonesty:** We will be checking your code against other submissions in the class for logical redundancy. If you copy someone else's code and submit it with minor changes, we will know. These cheat detectors are quite hard to fool, so please don't try. We trust you all to submit your own work only; please don't let us down. If you do, we will pursue the strongest consequences available to us.

## Hard margin SVM (20%)
### Load Dataset
Be sure to load and use the data in the following way (using a subset of IRIS data for completely isolated data). We only use 2 features of data.

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:100, :2]
y = iris.target[:100] 
```
<p>
  <img src = "https://github.com/MLDL-2024-GIST/Coding-Assignment/assets/79001832/026a92cf-81f6-4641-a54d-d11601ca73bf" width="400" height="300">
</p>

### Implement and Visualize 
`REPORT1`: Select an SVM from the visualized graph and use it to draw a decision boundary that perfectly separates the two datasets. The report should include a reasoned explanation of how the decision boundary was drawn based on the SVM.  


## Soft margin SVM (40%)
### Load Dataset
Be sure to load and use the data in the following way (using a subset of IRIS data for completely isolated data). We only use 2 features of data.

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[50:, 1:3]
y = iris.target[50:] 
```
### Implement and Visualize 
You can implement the soft margin SVM to predict the class with the input data.
```
>>> from SVM_soft import *
>>> model = SVM_soft(C=1.0) # set threshold value or 
>>> mode.fit(tr_x, tr_y)
>>> y_hat = model.predict(val_x)
>>> acc = computeClassificationAcc(val_y, y_hat) 
>>> print(acc)
0.6
```
`REPORT2`: Visualize the decision boundary of an SVM and analyze how slack variables allow misclassification. You can also adjust the hyperparameter 'C' to find best accuracy.

## Kernel Tricks (30%)
Write a program in python that performs Kernel Trick for SVM. Run your own kernel functions on the given dataset.
Visualize the decision boundaries and support vectors of each kernel filters.

### Load Dataset

```python
import sklearn

dataset = sklearn.datasets.make_moons(n_samples = 300, noise = 0.3, random_state = 20) # you can change noise and random_state where noise >= 0.15
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.3, random_state = 100)
```

<p>
  <img src = "https://github.com/MLDL-2024-GIST/Coding-Assignment/assets/97542056/1562d39f-c48d-47c5-8407-b53e0714f9f5" width="400" height="300">
</p>

### Implement and Visualize
`REPORT3`: Apply various kernel filters to SVM and compare their performance. Also, you have to visualize the decision boundaries and support vectors of SVM with different kernel filters. The report should indicate which kernel used in the SVM performed best, including reasons based on visualized data.

<p>
  <img src = "https://github.com/MLDL-2024-GIST/Coding-Assignment/assets/97542056/a9eb4119-35a3-4407-8170-c739b072f48b" width="400" height="300" >
</p>

## Discussion (10%)
`REPORT4`: Compare your implementation with `sklearn` library with same hyper-parameters.

## Extra Credit (30%)
You can earn extra credit for solving this question. 

### Optimize Quadratic Problem(QP) other than Gradient Descent Algorithm without using any library(except for cvxopt)
