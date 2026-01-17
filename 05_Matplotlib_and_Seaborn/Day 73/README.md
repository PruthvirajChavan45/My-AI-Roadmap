# 📘 Seaborn – Day 4  

## 📌 Topic: Regression & Mixed Plots  

Today I learned **Regression and Mixed plots in Seaborn**, which are used to analyze **relationships between variables**, understand **trends**, and visualize **multiple aspects of data together**. These plots are extremely useful during Exploratory Data Analysis (EDA) and statistical modeling.

---

## 🔹 `regplot()` – Scatter + Regression Line  

`regplot()` combines a **scatter plot with a fitted regression line**.

```python
sns.regplot(x="total_bill", y="tip", data=df)
```

Used for:
- Understanding linear relationships  
- Observing trend direction  
- Identifying correlation visually  

✔ Works with individual axes  
✔ Good for quick regression analysis  

---

## 🔹 `lmplot()` – Regression with Facets  

`lmplot()` is a higher-level interface built on `regplot()` that supports **faceting**.

```python
sns.lmplot(x="total_bill", y="tip", hue="sex", data=df)
```

Features:
- Multiple regression lines  
- Group-wise comparison  
- Automatic figure handling  

✔ Best for comparing regression across categories  

---

## 🔹 `jointplot()` – Scatter + Histogram / KDE  

`jointplot()` shows:
- Relationship between two variables  
- Distribution of each variable simultaneously  

```python
sns.jointplot(x="total_bill", y="tip", data=df, kind="scatter")
```

Other options:
```python
sns.jointplot(x="total_bill", y="tip", kind="kde", data=df)
sns.jointplot(x="total_bill", y="tip", kind="hex", data=df)
```

Useful for:
- Relationship + distribution analysis  
- Compact EDA views  

---

## 🔹 `pairplot()` – Relationships Between Many Variables  

`pairplot()` visualizes **pairwise relationships across multiple numeric columns**.

```python
sns.pairplot(df)
```

With grouping:
```python
sns.pairplot(df, hue="sex")
```

Used for:
- Multivariate analysis  
- Detecting correlations  
- Identifying patterns and clusters  

---

## 🔹 Which Plot to Use?

| Plot | Best Use Case |
|------|---------------|
| `regplot()` | Single regression analysis |
| `lmplot()` | Group-wise regression comparison |
| `jointplot()` | Relationship + distribution |
| `pairplot()` | Multi-variable relationship analysis |

---

## 🧠 Key Learnings (Day 4 – Seaborn)

- Visualized regression trends using `regplot()`  
- Compared regression across categories with `lmplot()`  
- Analyzed joint distributions using `jointplot()`  
- Explored multi-variable relationships using `pairplot()`  
- Improved understanding of correlation and patterns  

---

## 🎯 Outcome  

Day 4 strengthened my ability to:
- Analyze relationships visually  
- Understand regression behavior  
- Perform multivariate EDA  
- Create insightful and professional statistical plots  

---

✅ **Day 4 of Seaborn Completed Successfully 🚀**  

