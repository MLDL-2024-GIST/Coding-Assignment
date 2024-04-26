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

## Problem 1 (30%)
The objective is to employ Support Vector Machines (SVM) to find and visualize a decision boundary that perfectly classifies parts of the Iris dataset. This problem is not only about applying SVM but also understanding how its parameters affect the model's performance, especially under scenarios requiring perfect separation. Be sure to load and use the data in the following way (using a subset of IRIS data for completely isolated data)

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:100, :2]
y = iris.target[:100] 
```
<p>
  <img src = "https://github.com/MLDL-2024-GIST/Coding-Assignment/assets/79001832/026a92cf-81f6-4641-a54d-d11601ca73bf" width="400" height="300">
</p>

### (1) Data Preparation and Visualization  
Visualize the selected data in a scatter plot to understand the initial distribution. Highlight different classes using distinct colors and markers. This visualization will help you assess the feasibility of perfect separation with a linear boundary.   

### (2) Visualizing the decision boundary  
Select an SVM from the visualized graph and use it to draw a decision boundary that perfectly separates the two datasets. The report should include a reasoned explanation of how the decision boundary was drawn based on the SVM.   

### (3) Implementing Hard Margin SVM  
Adjust the SVM settings to enforce a hard margin (e.g., set the C parameter to a very high value). This configuration assumes that the data is linearly separable and aims to classify all training samples correctly without any misclassifications.  
Re-visualize the decision boundary. This visualization should now reflect a stricter separation where the margin is minimized to perfectly classify all training points.

## Problem 2 (40%)

## Problem 3 (30%)
Write a program in python that performs Kernel Trick for SVM. Run your own kernel functions on the given dataset.
Visualize the selected data in a scatter plot to understand the initial distribution. 

`REPORT3`: You must include all the following problems in the report to receive a full grade

```python
import sklearn

dataset = sklearn.datasets.make_moons(n_samples = 300, noise = 0.3, random_state = 20) # you can change noise and random_state but noise >= 0.15
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.3, random_state = 100)
```

<p>
  <img src = "https://github.com/MLDL-2024-GIST/Coding-Assignment/assets/97542056/1562d39f-c48d-47c5-8407-b53e0714f9f5" width="400" height="300">
</p>

### (1) Implementing Various Kernel Filters and Comparing Each Other
Apply various kernel filters to SVM and compare their performance.

### (2) Visualization the Decision Boundary and Support Vectors
Visualize the decision boundaries and support vectors of SVM with different kernel filters. The report should indicate which kernel used in the SVM performed best, including reasons based on visualized data.
<p>
  <img src = "https://github.com/MLDL-2024-GIST/Coding-Assignment/assets/97542056/a9eb4119-35a3-4407-8170-c739b072f48b" width="400" height="300" >
</p>

## Extra
You can earn extra credit (3 points) for solving this question. 

## 

(1)   
(2)
