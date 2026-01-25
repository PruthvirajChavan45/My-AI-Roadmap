
# 📘 Pandas – Day 8  

## 📌 Topic: Applying Pandas Concepts Through a Real-World Data Analysis Project  

On Day 8, I focused on **applying Pandas concepts in a real-world, large-scale data analysis project**. Instead of only practicing isolated functions, I worked on an end-to-end analysis workflow that reflects how Pandas is used in professional data analysis and data science environments.

---

## 🔗 Project Reference  

📊 **Student Performance Analysis Using Pandas**  
👉 GitHub Repository:  
https://github.com/PruthvirajChavan45/Student-Performance-Using-Pandas.git  

This project was used as a practical implementation of Pandas concepts learned so far.

---

## 🧠 Pandas Concepts Applied in This Project  

### 🔹 Data Loading & Validation  
- Loaded large CSV datasets efficiently  
- Verified schema and column consistency  
- Ensured scalability for large datasets  

```python
pd.read_csv("student_performance_sample.csv")
```

---

### 🔹 Dataset Inspection & Memory Analysis  
- Used `head()`, `info()`, `shape`, and `dtypes`  
- Analyzed memory usage for large datasets  
- Optimized data types for performance  

---

### 🔹 Handling Missing Values  
- Identified missing values  
- Applied appropriate strategies to handle them  

```python
df.isna()
df.fillna()
```

---

### 🔹 Data Type Optimization  
- Converted columns to efficient data types  
- Improved memory usage and processing speed  

```python
df["grade"] = df["grade"].astype("category")
```

---

### 🔹 Exploratory Data Analysis (EDA)  
- Explored distributions and patterns  
- Analyzed relationships between features  
- Understood student performance trends  

---

### 🔹 GroupBy & Aggregations  
- Grouped data by grades and performance categories  
- Calculated mean, count, and other aggregations  

```python
df.groupby("grade")["total_score"].mean()
```

---

### 🔹 Advanced Filtering & Conditional Selection  
- Applied complex filtering conditions  
- Identified high-performing and at-risk students  

```python
df[(df["attendance_percentage"] < 60) & (df["total_score"] < 50)]
```

---

### 🔹 Feature Engineering  
- Created new performance categories  
- Simplified analysis using derived columns  

```python
df["performance_level"] = df["total_score"].apply(
    lambda x: "High" if x >= 80 else "Low"
)
```

---

### 🔹 Insight Generation  
- Identified correlation between attendance, study hours, and scores  
- Extracted meaningful academic performance insights  
- Prepared data-driven conclusions  

---

## 🧪 Dataset Handling (Scalability Focus)

- Original dataset size: **1,000,000+ rows**  
- Sample dataset used for GitHub compatibility  
- All logic tested and validated on full-scale data  
- Analysis workflow scales without modification  

---

## 🧠 Key Learnings (Day 8)

- Applied Pandas in a real-world data analysis project  
- Worked with large datasets efficiently  
- Optimized memory and performance  
- Combined EDA, filtering, aggregation, and feature engineering  
- Transformed raw data into actionable insights  
- Practiced professional data analysis workflow  

---

## 🎯 Outcome  

Day 8 strengthened my ability to:
- Use Pandas in production-like scenarios  
- Handle large datasets confidently  
- Perform end-to-end data analysis  
- Write clean, scalable, and efficient Pandas code  
- Translate data into meaningful insights  

---

✅ **Day 8 of Pandas Completed Successfully 🚀**  
