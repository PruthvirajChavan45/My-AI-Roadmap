# 📘 Pandas – Day 2  

## 📌 Topic: Data Cleaning Essentials in Pandas  

On Day 2, I explored one of the most important parts of data analysis — **data cleaning and preprocessing**. Real-world data is often messy, and Pandas provides powerful tools to clean, transform, and prepare data for analysis.

---

## 🔹 Handling Missing Values  

Missing values are commonly represented as `NaN`. I learned multiple ways to detect and handle them.

### Detect Missing Values
```python
df.isna()
```

### Drop Missing Values
```python
df.dropna()
```

### Fill Missing Values
```python
df.fillna(value)
```

Used to:
- Remove incomplete records  
- Replace missing data with meaningful values  

---

## 🔹 Changing Data Types  

Correct data types are crucial for analysis and computation.

```python
df["column"].astype(int)
```

Used to:
- Convert strings to numeric values  
- Fix incorrect data types  
- Enable proper calculations  

---

## 🔹 Replacing Values  

Correcting typos or inconsistent values in data.

```python
df.replace(old_value, new_value)
```

Helpful for:
- Standardizing categorical data  
- Fixing spelling mistakes  
- Cleaning noisy data  

---

## 🔹 Dropping Rows & Columns  

Removing unnecessary or irrelevant data.

```python
df.drop(columns=["column_name"])
df.drop(index=[0, 1])
```

Used to:
- Remove extra columns  
- Delete unwanted rows  
- Reduce dataset size  

---

## 🔹 Detecting & Removing Duplicates  

Duplicate records can bias analysis.

### Detect Duplicates
```python
df.duplicated()
```

### Remove Duplicates
```python
df.drop_duplicates()
```

Ensures data uniqueness and accuracy.

---

## 🧪 Mini Practice (Hands-on Exercise)

To apply the learned concepts, I performed a mini practice exercise:

### Step 1: Create a Messy DataFrame
Included:
- Missing values  
- Wrong data types  
- Typographical errors  
- Extra columns  
- Duplicate rows  

---

### Step 2: Clean the Data Step-by-Step

✔ Handled missing values  
✔ Changed incorrect data types  
✔ Replaced incorrect or inconsistent values  
✔ Dropped unnecessary rows and columns  
✔ Removed duplicate records  

This practice helped simulate **real-world data cleaning scenarios**.

---

## 🧠 Key Learnings (Day 2)

- Handling missing values using `isna`, `dropna`, and `fillna`  
- Converting data types with `astype`  
- Replacing incorrect values using `replace`  
- Dropping rows and columns effectively  
- Detecting and removing duplicate data  
- Understanding real-world data cleaning workflows  

---

## 🎯 Outcome

Day 2 strengthened my understanding of **data preprocessing**, which is a critical step before:
- Exploratory Data Analysis (EDA)  
- Data visualization  
- Machine learning model building  

---

✅ **Day 2 of Pandas Completed Successfully 🚀**

