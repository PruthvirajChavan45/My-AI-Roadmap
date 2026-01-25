
# 📘 Pandas – Day 1  

## 📌 Topic: Pandas Introduction & DataFrame Basics  

Today marks my **first day of learning Pandas**, a powerful and essential Python library for **data analysis and data manipulation**. Pandas provides high-level data structures that make working with structured data fast, easy, and expressive.

---

## 📂 Folder Structure (As per Repository)

```
04_Pandas/
│
└── Day 60/
    ├── Pandas_Introduction.ipynb
    ├── DataFrame_Basics.ipynb
    ├── README.md
    └── Tasks.ipynb 
```

### 📁 Notebook Structure
1. **Pandas Introduction**  
2. **DataFrame Basics**
3. **Tasks**

---

## 🔹 What is Pandas?

Pandas is a **must-know Python library for data analysis**.  
It is widely used for:
- Data cleaning  
- Data manipulation  
- Data exploration  
- Data analysis workflows  

Pandas is built on top of **NumPy** and works seamlessly with other libraries like Matplotlib and Seaborn.

---

## 🔹 Core Data Structures in Pandas

### ✅ Series
- One-dimensional labeled data structure  
- Similar to a column in a table  

### ✅ DataFrame
- Two-dimensional labeled data structure  
- Similar to an Excel sheet or SQL table  

---

## 🔹 Creating Series & DataFrames

I practiced creating Pandas objects using multiple data sources:

- Python lists  
- Dictionaries  
- NumPy arrays  
- Introduction to loading data from CSV and Excel files  

---

## 🔹 Inspecting a DataFrame

Learned how to quickly understand and explore a dataset using:

```python
df.head()
df.tail()
df.info()
df.shape
df.dtypes
```

These methods help to:
- Preview data  
- Understand structure  
- Check data types  
- Identify missing values  

---

## 🔹 Selecting Data (Rows & Columns)

Practiced multiple ways to access data:

### Column Selection
```python
df["column_name"]
```

### Row Selection
```python
df.loc[row_label]
df.iloc[row_index]
```

- `[]` → basic selection  
- `.loc` → label-based indexing  
- `.iloc` → position-based indexing  

---

## 🔹 Index & Columns Exploration

Learned to:
- Understand index and column labels  
- Access index and column attributes  
- Modify structure for better analysis  

---

## 🔹 Renaming Columns

```python
df.rename(columns={"old_name": "new_name"})
```

Helps make datasets more readable and meaningful.

---

## 🔹 Setting & Resetting Index

```python
df.set_index("column_name")
df.reset_index()
```

Used to:
- Improve data alignment  
- Prepare data for analysis  
- Restructure DataFrames  

---

## 🧠 Key Learnings (Day 1 – Pandas)

- Understood what Pandas is and why it is used  
- Learned about Series and DataFrames  
- Created DataFrames from multiple data sources  
- Explored DataFrame inspection methods  
- Practiced row and column selection  
- Worked with index and columns  
- Renamed columns and managed index effectively  

---

## 🎯 Outcome

Day 1 built a **strong foundation in Pandas**, preparing me for:
- Data cleaning  
- Exploratory Data Analysis (EDA)  
- Data analysis projects  
- Advanced Pandas operations  

---

✅ **Day 1 of Pandas Completed Successfully 🚀**  

Next step → Advanced DataFrame operations & data analysis.
