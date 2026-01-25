
# 📘 NumPy – Day 8  

## 📌 Topic: Advanced NumPy Utility & Set Functions  

Today I learned and revised several important NumPy utility functions that are widely used for **data preprocessing, transformation, analysis, and feature engineering**. These functions help in sorting data, reshaping arrays, performing set operations, statistical calculations, and data filtering.

---

## 🔹 Sorting Arrays

### `np.sort()`
Sorts array elements in ascending order.

```python
np.sort([5, 2, 8, 1])
```

---

## 🔹 Append Elements

### `np.append()`
Adds elements to the end of an array.

```python
np.append([1, 2, 3], 4)
```

---

## 🔹 Concatenation

### `np.concatenate()`
Joins multiple arrays together.

```python
np.concatenate(([1, 2], [3, 4]))
```

---

## 🔹 Unique Values

### `np.unique()`
Returns sorted unique elements from an array.

```python
np.unique([1, 2, 2, 3, 3, 4])
```

---

## 🔹 Expand Dimensions

### `np.expand_dims()`
Adds a new axis to an array.

```python
arr = np.array([1, 2, 3])
np.expand_dims(arr, axis=0)
```

---

## 🔹 Conditional Selection

### `np.where()`
Returns indices or values based on condition.

```python
np.where(arr > 2, arr, 0)
```

---

## 🔹 Index of Maximum Value

### `np.argmax()`
Returns index of the maximum value.

```python
np.argmax([10, 50, 30])
```

---

## 🔹 Cumulative Sum

### `np.cumsum()`
Returns cumulative sum of elements.

```python
np.cumsum([1, 2, 3, 4])
```

---

## 🔹 Percentile

### `np.percentile()`
Computes the q-th percentile of data.

```python
np.percentile([10, 20, 30, 40], 50)
```

---

## 🔹 Histogram

### `np.histogram()`
Computes frequency distribution.

```python
np.histogram([1, 2, 2, 3, 3, 3], bins=3)
```

---

## 🔹 Correlation Coefficient

### `np.corrcoef()`
Measures correlation between arrays.

```python
np.corrcoef([1, 2, 3], [2, 4, 6])
```

---

## 🔹 Membership Checking

### `np.isin()`
Checks if elements exist in another array.

```python
np.isin([1, 2, 3], [2, 3])
```

---

## 🔹 Flip Array

### `np.flip()`
Reverses the order of elements.

```python
np.flip([1, 2, 3])
```

---

## 🔹 Replace Values by Index

### `np.put()`
Replaces values at specified indices.

```python
arr = np.array([10, 20, 30])
np.put(arr, [0, 2], [100, 300])
```

---

## 🔹 Delete Elements

### `np.delete()`
Removes elements by index.

```python
np.delete([10, 20, 30], 1)
```

---

## 🔹 Set Operations in NumPy

### Union
```python
np.union1d([1, 2, 3], [3, 4, 5])
```

### Intersection
```python
np.intersect1d([1, 2, 3], [2, 3, 4])
```

### Difference
```python
np.setdiff1d([1, 2, 3], [2])
```

### Symmetric Difference
```python
np.setxor1d([1, 2, 3], [2, 4])
```

### Membership Test
```python
np.in1d([1, 2, 3], [2, 4])
```

---

## 🔹 Clipping Values

### `np.clip()`
Limits values within a specified range.

```python
np.clip([1, 5, 10, 15], 3, 10)
```

---

## 🧠 Key Learnings (Day 8)

- Sorting and modifying arrays  
- Appending and concatenating arrays  
- Finding unique values  
- Reshaping arrays using expand_dims  
- Conditional selection using `where`  
- Statistical functions like percentile & correlation  
- Working with histograms  
- Membership testing and set operations  
- Value replacement and deletion  
- Clipping values within a range  

---

## 🎯 Outcome

This day strengthened my understanding of **advanced NumPy utility functions** that are essential for:

- Data preprocessing  
- Feature engineering  
- Statistical analysis  
- Data cleaning  
- Machine learning workflows  

✅ **Day 8 Completed Successfully — Advanced NumPy Utilities**
