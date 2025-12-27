# 📘 NumPy – Array Basics (Day – 2)

## 📌 Topic Covered
Today I learned the basic concepts of NumPy arrays, including array attributes, indexing, slicing, boolean indexing, reshaping, and flattening.

---

## 📍 Array Attributes  
NumPy arrays have important attributes that help us understand their structure:

- **shape** → returns the dimensions of the array (rows, columns)  
- **ndim** → returns the number of dimensions of the array  
- **size** → returns the total number of elements in the array  
- **dtype** → shows the data type of elements stored in the array  

These attributes help in understanding how data is organized inside an array.

---

## 📍 Indexing  
Indexing is used to access specific elements of an array using their position.

- Index starts from **0**
- Negative indexing starts from the end  
- Works for both 1D and multi-dimensional arrays  

Indexing allows accessing a single value from the array.

---

## 📍 Slicing  
Slicing is used to extract a **portion of an array**.

Syntax:
```
array[start : stop : step]
```

- Start → starting index  
- Stop → ending index (excluded)  
- Step → gap between elements  

Slicing helps in selecting ranges of values easily.

---

## 📍 Boolean Indexing  
Boolean indexing is used to filter elements based on a condition.

- Condition returns `True` or `False`
- Only elements satisfying the condition are selected  

This is useful for filtering data based on rules.

---

## 📍 Reshaping the Array  
Reshaping changes the **shape of an array without changing its data**.

- Total number of elements must remain the same  
- Commonly used to convert 1D array into 2D or higher dimensions  

Used in data preprocessing and machine learning.

---

## 📍 Flattening an Array  
Flattening converts a **multi-dimensional array into a 1D array**.

- All elements are placed into a single row  
- Useful when algorithms require one-dimensional input  

---

✅ This lesson builds the foundation for efficient data manipulation using NumPy arrays.
```

