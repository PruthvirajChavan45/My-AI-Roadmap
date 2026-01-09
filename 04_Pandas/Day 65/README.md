# 📘 Pandas – Day 6  

## 📌 Topic: Merging, Joining & Concatenation  

On Day 6, I learned how to **combine multiple DataFrames** using Pandas. These techniques are essential when working with real-world data spread across multiple tables, similar to SQL databases.

---

## 🔹 Using `concat()` for Stacking Data  

`pd.concat()` is used to combine DataFrames **row-wise or column-wise**.

### Vertical Stacking (Rows)
```python
pd.concat([df1, df2], axis=0)
```

### Horizontal Stacking (Columns)
```python
pd.concat([df1, df2], axis=1)
```

### Reset Index after Concatenation
```python
pd.concat([df1, df2], ignore_index=True)
```

Used when:
- Appending datasets  
- Combining similar DataFrames  
- Stacking time-based data  

---

## 🔹 Using `merge()` for SQL-Style Joins  

`merge()` works like SQL joins and is used to combine DataFrames based on **key columns**.

### Basic Merge
```python
pd.merge(df1, df2, on="id")
```

### Merge with Different Key Names
```python
pd.merge(df1, df2, left_on="emp_id", right_on="id")
```

### Join Types
```python
pd.merge(df1, df2, how="inner")
pd.merge(df1, df2, how="left")
pd.merge(df1, df2, how="right")
pd.merge(df1, df2, how="outer")
```

Used to:
- Link related datasets  
- Combine tables like SQL  
- Handle missing matches  

---

## 🔹 Using `join()` with Index Alignment  

`join()` combines DataFrames using **index alignment** by default.

### Join on Index
```python
df1.join(df2)
```

### Join on a Column
```python
df1.join(df2.set_index("id"), on="id")
```

Useful for:
- Adding columns to an existing DataFrame  
- Working with index-based data  

---

## 🔹 Practical Examples  

- Combined **sales and revenue** data to analyze performance  
- Merged **student details with marks**  
- Practiced joins to understand:
  - Data alignment  
  - Missing values after joins  
  - Join behavior across datasets  

---

## 🧪 Mini Practice (Hands-on Tasks)

### Task Setup
Created three DataFrames:
- `Products`
- `Sales`
- `Revenue`

---

### Practice Steps

**1️⃣ Concatenate DataFrames**
```python
pd.concat([products, sales], axis=0)
pd.concat([products, sales], axis=1)
```

**2️⃣ Merge Sales & Revenue**
```python
pd.merge(sales, revenue, on="product_id", how="inner")
pd.merge(sales, revenue, on="product_id", how="left")
pd.merge(sales, revenue, on="product_id", how="right")
pd.merge(sales, revenue, on="product_id", how="outer")
```

**3️⃣ Join Products with Sales**
```python
products.join(sales, on="product_id")
```

**4️⃣ Analyze Missing Values**
```python
merged_df.isna()
```

---

## 🧠 Key Learnings (Day 6)

- Combined DataFrames using `concat()`  
- Performed SQL-style joins using `merge()`  
- Used `join()` for index-based alignment  
- Understood different join types and their outcomes  
- Analyzed missing values after joins  
- Practiced with realistic datasets  

---

## 🎯 Outcome  

Day 6 strengthened my understanding of **data integration in Pandas**, which is critical for:
- Real-world data analysis  
- Database-like operations  
- Data preprocessing pipelines  
- Feature engineering  

---

✅ **Day 6 of Pandas Completed Successfully 🚀**
```

