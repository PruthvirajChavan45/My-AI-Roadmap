# 📘 NumPy – Day 6  

## 📌 Topic: NumPy Fundamentals Revision  

On Day 6, I revised the core concepts of NumPy to strengthen my foundation in array manipulation, indexing, and data handling. This revision focuses on understanding how NumPy works internally and how to efficiently operate on arrays for data analysis and future machine learning tasks.

---

## ✅ Topics Covered in This Revision

---

## 🔹 Array Creation

Creating NumPy arrays using different methods:

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
```

Other commonly used creation methods:
```python
np.zeros(5)
np.ones(5)
np.arange(0, 10)
np.linspace(1, 10, 5)
```

---

## 🔹 Array Attributes

Understanding the structure and properties of NumPy arrays:

```python
arr.shape
arr.ndim
arr.size
arr.dtype
```

These attributes help to:
- Know array dimensions  
- Count total elements  
- Identify data type  
- Understand array structure  

---

## 🔹 Indexing

Accessing elements using index positions:

```python
arr[0]
arr[-1]
```

Used to fetch specific elements from an array.

---

## 🔹 Slicing

Extracting a portion of an array:

```python
arr[1:4]
arr[:3]
arr[::2]
```

Useful for working with subsets of data.

---

## 🔹 Fancy Indexing

Selecting multiple elements using a list of indices:

```python
arr[[0, 2, 4]]
```

Helps in selecting non-contiguous values directly.

---

## 🔹 Conditional Selection (Boolean Indexing)

Filtering elements based on conditions:

```python
arr[arr > 10]
```

Using condition variables:

```python
condition = arr % 2 == 0
arr[condition]
```

Used heavily in data cleaning and filtering operations.

---

## 🔹 Sorting and Ordering

Sorting values in an array:

```python
np.sort(arr)
```

Getting index order of sorted elements:

```python
np.argsort(arr)
```

Sorting in 2D arrays:

```python
np.sort(arr, axis=0)
np.sort(arr, axis=1)
```

---

## 🔹 Concatenation

Combining multiple arrays into one:

```python
np.concatenate((a, b))
```

Helpful when merging datasets.

---

## 🔹 Vertical and Horizontal Stacking

### Vertical Stacking
```python
np.vstack((a, b))
```

### Horizontal Stacking
```python
np.hstack((a, b))
```

Used to combine arrays row-wise or column-wise.

---

## 🧠 Key Learnings from Day 6

- Revised NumPy array fundamentals  
- Strengthened indexing and slicing concepts  
- Learned fancy indexing and conditional selection  
- Practiced sorting and ordering techniques  
- Understood concatenation and stacking operations  
- Improved confidence in array manipulation  
- Built strong foundation for Pandas and data analysis  

---

## 🎯 Outcome

This revision helped reinforce core NumPy concepts that are essential for:
- Data analysis  
- Data preprocessing  
- Machine learning workflows  
- Writing clean and efficient Python code  

---

✅ **Day 6 Completed – NumPy Fundamentals Revision Successfully**

