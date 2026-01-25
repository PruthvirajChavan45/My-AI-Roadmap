# 📘 Pandas – Day 3  

## 📌 Topic: Data Selection & Filtering  

On Day 3, I learned how to **select, filter, and clean data efficiently in Pandas**. These techniques are essential for exploratory data analysis (EDA) and real-world data preprocessing, where we often need to extract specific subsets of data based on conditions.

---

## 🔹 Boolean Indexing & Conditional Selection  

Boolean indexing allows filtering rows using conditions built with comparison operators.

### Building Conditions
```python
df["Score"] > 50
```

### Applying Conditions
```python
df[df["Score"] > 50]
```

### Combining Multiple Conditions
```python
df[(df["Age"] > 25) & (df["Score"] >= 80)]
df[(df["City"] == "Delhi") | (df["City"] == "Mumbai")]
df[~(df["Age"] < 18)]
```

📌 **Important Rule:**  
Parentheses are required when combining conditions using `&`, `|`, and `~`.

---

## 🔹 Filtering Rows with Multiple Conditions  

Multiple conditions help refine data selection more precisely.

```python
df[(df["Age"] > 25) & (df["City"] == "Delhi")]
```

Used to:
- Narrow down datasets  
- Apply business rules  
- Perform targeted analysis  

---

## 🔹 Using `query()` for Cleaner Filtering  

The `query()` method provides a cleaner and more readable way to filter rows using string expressions.

```python
df.query("Score >= 85 and Age < 35")
```

### Using External Variables
```python
min_score = 85
df.query("Score >= @min_score")
```

✔ More readable  
✔ Useful for complex filtering  
✔ Reduces bracket-heavy syntax  

---

## 🔹 String Operations on Columns  

Pandas provides vectorized string operations using the `.str` accessor.

### Common String Methods
```python
df["Name"].str.contains("a")
df["City"].str.replace("New", "")
df["Name"].str.lower()
df["Name"].str.upper()
df["City"].str.startswith("M")
df["City"].str.endswith("i")
```

Used for:
- Text cleaning  
- Standardizing data  
- Filtering text-based columns  

---

## 🧪 Mini Practice (Hands-on Tasks)

### Task Setup
Created a DataFrame with columns:
- `Name`
- `Age`
- `City`
- `Score`

---

### Practice Steps

**i) Select rows where Age > 25**
```python
df[df["Age"] > 25]
```

**ii) Filter rows where City is Delhi or Mumbai**
```python
df[(df["City"] == "Delhi") | (df["City"] == "Mumbai")]
```

**iii) Use `query()` for Score ≥ 85 and Age < 35**
```python
df.query("Score >= 85 and Age < 35")
```

**iv) Clean text column**
```python
df["Name"] = df["Name"].str.lower()
```

---

## 🧠 Key Learnings (Day 3)

- Used boolean indexing for conditional selection  
- Combined multiple conditions using logical operators  
- Applied `query()` for clean and readable filtering  
- Worked with vectorized string operations  
- Cleaned and filtered text-based data  
- Practiced real-world style filtering tasks  

---

## 🎯 Outcome  

Day 3 strengthened my ability to **filter and clean data efficiently**, a critical skill for:
- Exploratory Data Analysis (EDA)  
- Data preprocessing  
- Feature selection  
- Real-world data analysis workflows  

---

✅ **Day 3 of Pandas Completed Successfully 🚀**

