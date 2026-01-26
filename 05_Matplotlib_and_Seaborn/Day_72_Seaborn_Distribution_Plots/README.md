# 📘 Seaborn – Day 3  

## 📌 Topic: Distribution Plots in Seaborn  

Today I learned **Distribution Plots**, which are used to understand **how data is distributed** across values. These plots are a core part of Exploratory Data Analysis (EDA) and help identify patterns such as spread, skewness, peaks, and density.

---

## 🔹 What Are Distribution Plots?

Distribution plots visualize:
- Frequency of data points  
- Spread of values  
- Shape of data (normal, skewed, multimodal)  

They are especially useful for:
- Understanding numeric data  
- Detecting skewness and outliers  
- Comparing distributions  

---

## 🔹 `histplot()` – Basic Histogram  

`histplot()` is used to visualize the **frequency distribution** of numerical data.

```python
sns.histplot(data=df, x="total_bill", bins=20)
```

Shows:
- Count of values in each bin  
- Overall data distribution  

✔ Most commonly used distribution plot  
✔ Highly customizable  

---

## 🔹 `kdeplot()` – Kernel Density Estimate  

`kdeplot()` shows a **smooth probability density curve** instead of bars.

```python
sns.kdeplot(data=df, x="total_bill")
```

Useful for:
- Understanding data density  
- Identifying peaks and spread  
- Comparing smooth distributions  

---

## 🔹 `distplot()` (Legacy) vs `histplot()`  

⚠️ `distplot()` is **deprecated** and should not be used in new code.

❌ Old (Deprecated):
```python
sns.distplot(df["total_bill"])
```

✅ Recommended Alternatives:
```python
sns.histplot(df["total_bill"])
sns.kdeplot(df["total_bill"])
```

✔ `histplot()` → histogram  
✔ `kdeplot()` → density curve  

---

## 🔹 `rugplot()` – Small Ticks for Observations  

`rugplot()` adds small ticks on the axis to show **individual observations**.

```python
sns.rugplot(data=df, x="total_bill")
```

Often combined with:
- Histogram  
- KDE plot  

Helps visualize exact data points.

---

## 🔹 Multiple Distributions with `hue`  

The `hue` parameter allows comparison of **multiple distributions** in one plot.

```python
sns.histplot(data=df, x="total_bill", hue="sex", kde=True)
```

Useful for:
- Group-wise comparison  
- Identifying differences between categories  

---

## 🔹 Which Distribution Plot to Use?

| Plot | Best For |
|-----|---------|
| `histplot()` | Frequency & spread |
| `kdeplot()` | Smooth density estimation |
| `rugplot()` | Individual data points |
| `histplot()` + `hue` | Comparing multiple distributions |

---

## 🧠 Key Learnings (Day 3 – Seaborn)

- Understood what distribution plots represent  
- Created histograms using `histplot()`  
- Visualized density using `kdeplot()`  
- Learned why `distplot()` is deprecated  
- Used `rugplot()` for observation-level detail  
- Compared multiple distributions using `hue`  

---

## 🎯 Outcome  

Day 3 improved my ability to **analyze and compare data distributions**, which is essential for:
- Exploratory Data Analysis (EDA)  
- Statistical understanding  
- Data-driven decision making  

---

✅ **Day 3 of Seaborn Completed Successfully 🚀**  
