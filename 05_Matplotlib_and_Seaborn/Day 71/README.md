# 📘 Seaborn – Day 2  

## 📌 Topic: Categorical Plots in Seaborn  

Today I learned **Categorical Plots in Seaborn**, which are used to visualize **relationships between a categorical variable and a numerical variable** (or counts of categories). These plots are extremely useful in Exploratory Data Analysis (EDA) to compare groups and understand data distribution.

---

## 🔹 What Are Categorical Plots?

Categorical plots are used when:
- One axis represents **categorical data** (e.g., gender, city, department)
- The other axis represents **numerical data** or **counts**

They help in:
- Comparing groups  
- Understanding distributions  
- Detecting outliers  
- Summarizing data visually  

---

## 🔹 `barplot()` vs `countplot()`

### 🔸 `barplot()`
- Shows **aggregated values** (mean by default)
- Used when you want to compare **numeric values across categories**

```python
sns.barplot(x="day", y="total_bill", data=df)
```

✔ Shows average (or other estimator)  
✔ Supports confidence intervals  

---

### 🔸 `countplot()`
- Shows **frequency/count of categories**
- Used when you want to count occurrences

```python
sns.countplot(x="day", data=df)
```

✔ No numeric column required  
✔ Best for categorical frequency analysis  

---

## 🔹 `boxplot()` & `violinplot()`

### 🔸 `boxplot()`
- Displays data distribution using quartiles
- Helps detect **outliers**

```python
sns.boxplot(x="day", y="total_bill", data=df)
```

Shows:
- Median  
- Quartiles  
- Outliers  

---

### 🔸 `violinplot()`
- Combines boxplot with density estimation
- Shows **distribution shape**

```python
sns.violinplot(x="day", y="total_bill", data=df)
```

✔ Better for understanding distribution  
✔ Useful when data size is large  

---

## 🔹 `stripplot()` & `swarmplot()`

### 🔸 `stripplot()`
- Displays all data points
- Points may overlap

```python
sns.stripplot(x="day", y="total_bill", data=df)
```

✔ Simple and fast  
❌ Overlapping points  

---

### 🔸 `swarmplot()`
- Displays data points **without overlap**
- More readable than stripplot

```python
sns.swarmplot(x="day", y="total_bill", data=df)
```

✔ Clear visualization  
❌ Slower for large datasets  

---

## 🔹 Which Plot is Best For What?

| Plot Type | Best Used For |
|----------|--------------|
| `barplot()` | Comparing average values across categories |
| `countplot()` | Counting category frequencies |
| `boxplot()` | Detecting outliers & spread |
| `violinplot()` | Understanding data distribution |
| `stripplot()` | Viewing individual data points |
| `swarmplot()` | Clear individual data point comparison |

---

## 🧠 Key Learnings (Day 2 – Seaborn)

- Understood the purpose of categorical plots  
- Learned differences between barplot & countplot  
- Analyzed data distribution using boxplot & violinplot  
- Visualized individual data points using stripplot & swarmplot  
- Chose the right plot based on analysis requirement  

---

## 🎯 Outcome  

Day 2 strengthened my ability to **compare categories visually**, which is essential for:
- Exploratory Data Analysis (EDA)  
- Business insights  
- Data storytelling  
- Statistical comparison  

---

✅ **Day 2 of Seaborn Completed Successfully 🚀**  

