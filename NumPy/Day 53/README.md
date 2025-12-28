# 📘 NumPy – Day 3  
## 📌 Topic: Array Operations, Broadcasting & Aggregate Functions 

## 📌 NumPy Array Operations
NumPy supports fast element-wise operations on arrays. These operations are applied to each element without using loops.

### Arithmetic Operations
- Addition: `a + b`
- Subtraction: `a - b`
- Multiplication: `a * b`
- Division: `a / b`
- Power: `a ** b`
These operations work element-wise between arrays of the same shape or compatible shapes.

### Comparison Operations
- `a > b`
- `a < b`
- `a == b`
- `a != b`
They return boolean arrays.

---

## 📌 Broadcasting
Broadcasting allows NumPy to perform operations on arrays of **different shapes** by automatically expanding the smaller array.

### Broadcasting Rules:
1. If array dimensions are not equal, the smaller one is padded with 1s on the left.
2. Dimensions are compatible if:
   - they are equal, or  
   - one of them is 1
3. NumPy stretches the dimension with size 1 to match the other.

### Example Idea:
- Array shape (3, 3) + scalar (1)
- Scalar is broadcast to all elements
- Operation happens element-wise

Broadcasting avoids loops and makes computation faster.

---

## 📌 Aggregate Functions
Aggregate functions summarize data into a single value.

Common aggregate functions in NumPy:
- `sum()` → total of elements
- `mean()` → average value
- `min()` → smallest value
- `max()` → largest value
- `std()` → standard deviation
- `var()` → variance
- `median()` → middle value
- `argmin()` → index of minimum value
- `argmax()` → index of maximum value

### Axis Usage:
- `axis=0` → column-wise operation  
- `axis=1` → row-wise operation  

Aggregate functions help in:
- statistical analysis  
- data summarization  
- understanding distribution  
- preprocessing before ML  

---
```

