# 📘 Pandas – Day 4  

## 📌 Topic: Sorting & Basic Statistics  

On Day 4, I focused on **sorting data and performing basic statistical analysis using Pandas**. These operations are essential for understanding data distribution, identifying patterns, and preparing data for deeper analysis.

---

## 🔹 Sorting Data  

Sorting helps organize data in a meaningful order.

### Sort by Column Values
```python
df.sort_values(by="Score")
```

### Sort in Descending Order
```python
df.sort_values(by="Score", ascending=False)
```

### Sort by Multiple Columns
```python
df.sort_values(by=["Score", "Age"], ascending=[False, True])
```

### Sort by Index
```python
df.sort_index()
```

Used to:
- Rank data  
- Identify top/bottom values  
- Prepare ordered datasets  

---

## 🔹 Descriptive Statistics  

Descriptive statistics summarize and describe numerical data.

### Central Tendency
```python
df.mean()
df.median()
df.mode()
```

### Dispersion
```python
df.std()
```

### Statistical Summary
```python
df.describe()
```

Provides:
- Count  
- Mean  
- Standard deviation  
- Minimum & maximum  
- Quartiles  

---

## 🔹 Counting Values  

### Frequency Count
```python
df["Name"].value_counts()
```

### Percentage Distribution
```python
df["Name"].value_counts(normalize=True)
```

Used to:
- Analyze categorical data  
- Identify most frequent values  
- Understand distribution  

---

## 🔹 Correlation & Covariance  

### Correlation
```python
df.corr()
```

- Measures relationship strength between numeric columns  
- Values range from **-1 to +1**  

### Covariance
```python
df.cov()
```

- Measures how two variables change together  

Used in:
- Feature analysis  
- Understanding relationships between variables  

---

## 🧪 Mini Practice (Hands-on Tasks)

### Task Setup
Created a DataFrame with columns:
- `Name`
- `Age`
- `Score`
- `Height`

---

### Practice Steps

**1️⃣ Sort data by Score (descending)**
```python
df.sort_values(by="Score", ascending=False)
```

**2️⃣ Calculate statistics**
```python
df.mean()
df.median()
df.mode()
df.std()
```

**3️⃣ Count values in categorical column**
```python
df["Name"].value_counts()
```

**4️⃣ Compute correlation & covariance**
```python
df.corr()
df.cov()
```

---

## 🧠 Key Learnings (Day 4)

- Sorted data using values and index  
- Applied descriptive statistical methods  
- Analyzed categorical data using value counts  
- Understood correlation and covariance  
- Practiced statistical analysis on real data  

---

## 🎯 Outcome  

Day 4 strengthened my understanding of **data ordering and statistical analysis**, which is crucial for:
- Exploratory Data Analysis (EDA)  
- Data insights & reporting  
- Feature selection  
- Data-driven decision making  

---

✅ **Day 4 of Pandas Completed Successfully 🚀**

