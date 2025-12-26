# 📘 NumPy – Day 1  

## 📌 Topic: Introduction to NumPy and Array Creation  

NumPy (Numerical Python) is a powerful Python library used for numerical computing. It is mainly used to work with arrays and perform fast mathematical operations. NumPy is the foundation for data science, machine learning, and scientific computing in Python.

NumPy provides an efficient data structure called **ndarray (N-dimensional array)** which is faster and more memory-efficient than Python lists.

---

## 📍 Why NumPy is Used  
- Handles large numerical datasets efficiently  
- Faster than Python lists  
- Supports multi-dimensional arrays  
- Used in data analysis, ML, AI, and scientific computing  
- Works well with libraries like Pandas, Matplotlib, and Scikit-learn  

---

## 📍 Creating NumPy Array  

To use NumPy, first import it:
```python
import numpy as np
```

### 1. Creating array from a Python list
```python
arr = np.array([1, 2, 3, 4])
```

### 2. Creating a 2D array
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
```

### 3. Creating array using zeros()
Creates an array filled with zeros.
```python
np.zeros(5)
```

### 4. Creating array using ones()
Creates an array filled with ones.
```python
np.ones(4)
```

### 5. Creating array using arange()
Creates values within a given range.
```python
np.arange(0, 10)
```

### 6. Creating array using linspace()
Creates evenly spaced values between two numbers.
```python
np.linspace(1, 10, 5)
```

### 7. Creating array with specific data type
```python
np.array([1, 2, 3], dtype=float)
```

---

## 📍 Summary  
- NumPy is used for numerical and array-based computation  
- Arrays are the core data structure in NumPy  
- Arrays can be created using lists or built-in NumPy functions  
- NumPy makes data processing faster and more efficient  

---

