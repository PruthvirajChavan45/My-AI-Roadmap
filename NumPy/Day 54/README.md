# 📘 NumPy – Day 4  

## 📌 Topic: Advanced Indexing and Manipulation  

Today I learned advanced NumPy techniques used to access, filter, sort, and combine arrays efficiently. These concepts are very important for real-world data manipulation and analysis.

---

## 📍 Fancy Indexing  

Fancy indexing allows selecting elements using a list or array of index positions.

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print("Fancy indexing:", arr[[0, 2, 4]])
```

### Output
```
[10 30 50]
```

### Fancy Indexing in 2D Array

```python
matrix = np.arange(1, 13).reshape(3, 4)
print("Selected elements:", matrix[[0, 1], [1, 2]])
```

This selects:
- row 0, column 1  
- row 1, column 2  

---

## 📍 Conditional Selection  

Conditional selection is used to filter or modify values based on conditions.

```python
arr = np.array([5, 12, 18, 7, 30])

# if value > 10 keep it, else replace with 0
print(np.where(arr > 10, arr, 0))
```

### Output
```
[ 0 12 18  0 30]
```

This helps in filtering, masking, and conditional replacement.

---

## 📍 Sorting and Ordering  

### Sorting values using `np.sort()`

```python
arr = np.array([42, 5, 18, 23])
print("Sorted:", np.sort(arr))
```

### Getting sorted index positions using `np.argsort()`

```python
idx = np.argsort(arr)
print("Indices:", idx)
print("Using indices:", arr[idx])
```

---

### Sorting in 2D Arrays

```python
mat = np.array([[3, 7, 1],
                [9, 4, 6]])

print(np.sort(mat, axis=1))   # sort each row
print(np.sort(mat, axis=0))   # sort each column
```

---

## 📍 Concatenation  

Concatenation is used to join multiple arrays into one.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.concatenate((a, b)))
```

### Output
```
[1 2 3 4 5 6]
```

---

## 📍 Vertical Stacking (vstack)  

Stacks arrays vertically (row-wise).

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.vstack((a, b)))
```

### Output
```
[[1 2 3]
 [4 5 6]]
```

---

## 📍 Horizontal Stacking (hstack)  

Stacks arrays horizontally (column-wise).

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.hstack((a, b)))
```

### Output
```
[1 2 3 4 5 6]
```

---

## 📍 Summary  

- Fancy indexing selects elements using index lists  
- Conditional selection filters or replaces values using conditions  
- `np.sort()` sorts array values  
- `np.argsort()` returns index order  
- Concatenation joins arrays together  
- Vertical stacking combines arrays row-wise  
- Horizontal stacking combines arrays column-wise  

These advanced indexing and manipulation techniques help in efficient data preprocessing and analysis using NumPy.

