# 📘 NumPy – Day 7  

## 📌 Topic: NumPy vs Python Lists, Advanced Indexing, Broadcasting, Mathematical Operations & Visualization (Intro)

On Day 7, I learned and revised important intermediate NumPy concepts that are widely used in data analysis, machine learning, and numerical computing. This includes comparison with Python lists, indexing techniques, broadcasting, mathematical formulas, handling missing values, and basic plotting concepts.

---

## 🔹 NumPy Array vs Python List

### Python List
- Can store different data types  
- Slower for numerical operations  
- Less memory efficient  
- No built-in vectorized operations  

### NumPy Array
- Stores elements of the same data type  
- Faster and memory efficient  
- Supports vectorized operations  
- Designed for numerical computation  

Example:
```python
import numpy as np

lst = [1, 2, 3]
arr = np.array([1, 2, 3])
```

---

## 🔹 Indexing in NumPy

### Normal Indexing
Access elements using index positions.

```python
arr[0]
arr[-1]
arr[1:4]
```

---

## 🔹 Fancy Indexing

Select elements using a list or array of indices.

```python
arr[[0, 2, 4]]
```

Useful when selecting non-contiguous elements.

---

## 🔹 Broadcasting

Broadcasting allows NumPy to perform operations on arrays of different shapes automatically.

Example:
```python
arr = np.array([1, 2, 3])
arr + 5
```

Output:
```
[6 7 8]
```

Broadcasting avoids loops and improves performance.

---

## 🔹 Broadcasting Rules

1. If array dimensions are different, the smaller one is padded with 1s on the left  
2. Dimensions must be equal or one of them must be 1  
3. NumPy stretches the smaller array to match the larger one  
4. Operation is performed element-wise  

---

## 🔹 Working with Mathematical Formulas

### Sigmoid Function
Used in machine learning and logistic regression.

```python
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
```

---

### Mean Squared Error (MSE)
Used to measure error between actual and predicted values.

```python
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)
```

---

## 🔹 Working with Missing Values (Introduction)

Missing values are usually represented using `np.nan`.

```python
arr = np.array([10, 20, np.nan, 40])
```

Checking missing values:
```python
np.isnan(arr)
```

Handling missing values:
```python
np.nanmean(arr)
```

---

## 🔹 Plotting Graphs (NumPy + Matplotlib – Intro)

Basic plotting using NumPy and Matplotlib.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10)
y = x ** 2

plt.plot(x, y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Simple Line Plot")
plt.show()
```

Used to visualize data and understand patterns easily.

---

## 🧠 Key Learnings from Day 7

- Difference between NumPy arrays and Python lists  
- Normal vs fancy indexing  
- Broadcasting and its rules  
- Applying mathematical formulas using NumPy  
- Understanding sigmoid and MSE  
- Handling missing values with NumPy  
- Basics of plotting using Matplotlib  

---

## 🎯 Outcome

Day 7 strengthened my understanding of how NumPy works behind the scenes and how it connects mathematical operations, data cleaning, and visualization — essential skills for data analysis and machine learning.

✅ **Day 7 Completed Successfully**

