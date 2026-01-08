# 📘 Pandas – Day 5  

## 📌 Topic: GroupBy & Aggregations 

On Day 5, I learned how to **summarize and analyze data using GroupBy and aggregation techniques in Pandas**. These concepts are fundamental for real-world data analysis, reporting, and business insights.

---

## 🔹 Concept of Split–Apply–Combine  

This is the core idea behind `groupby()` in Pandas.

1. **Split** – Divide data into groups based on a column  
2. **Apply** – Apply a function (sum, mean, count, etc.) to each group  
3. **Combine** – Combine results into a new DataFrame or Series  

Example:
```python
df.groupby("Department")["Salary"].mean()
```

---

## 🔹 Using `groupby()` with Aggregation Functions  

Aggregation functions help summarize data for each group.

```python
df.groupby("Department").mean()
df.groupby("Department").sum()
df.groupby("Department").count()
df.groupby("Department").min()
df.groupby("Department").max()
```

---

## 🔹 Multiple Aggregations using `agg()`  

The `agg()` function allows applying **multiple aggregation functions at once**.

```python
df.groupby("Department").agg(["mean", "max", "count"])
```

---

## 🔹 Multiple Aggregations on Different Columns  

Different columns can have different aggregation functions.

```python
df.groupby("Department").agg({
    "Salary": "mean",
    "Age": "max"
})
```

This is useful for creating **custom summaries**.

---

## 🔹 Pivot Tables  

Pivot tables summarize data similar to Excel pivot tables.

```python
pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="City",
    aggfunc="mean"
)
```

Used to:
- Compare metrics across groups  
- Analyze multi-dimensional data  

---

## 🔹 Crosstab  

Crosstab is used to calculate frequency counts of combinations.

```python
pd.crosstab(df["Department"], df["City"])
```

Used to:
- Analyze categorical relationships  
- Count occurrences across categories  

---

## 🧪 Mini Practice (Hands-on Tasks)

### Task Setup
Created a DataFrame with columns:
- `Department`
- `Employee`
- `Salary`
- `Age`
- `City`

---

### Practice Steps

**1️⃣ Average Salary & Max Age by Department**
```python
df.groupby("Department").agg({
    "Salary": "mean",
    "Age": "max"
})
```

**2️⃣ Apply multiple aggregations**
```python
df.groupby("Department").agg(["mean", "count"])
```

**3️⃣ Pivot Table (Mean Salary by Department & City)**
```python
pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="City",
    aggfunc="mean"
)
```

**4️⃣ Crosstab (Department vs City)**
```python
pd.crosstab(df["Department"], df["City"])
```

---

## 🧠 Key Learnings (Day 5)

- Understood the Split–Apply–Combine strategy  
- Used `groupby()` for data summarization  
- Applied single and multiple aggregation functions  
- Performed column-wise aggregations using `agg()`  
- Created pivot tables for multi-dimensional analysis  
- Built crosstabs for categorical comparison  

---

## 🎯 Outcome  

Day 5 strengthened my ability to **analyze grouped data**, which is critical for:
- Business analytics  
- Reporting dashboards  
- Data summarization  
- Exploratory Data Analysis (EDA)  

---

✅ **Day 5 of Pandas Completed Successfully 🚀**

