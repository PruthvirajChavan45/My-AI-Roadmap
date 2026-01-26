# 📘 Seaborn – Day 1  

## 📌 Topic: Seaborn Introduction & Relational Plots  

Today I covered the **fundamentals of Seaborn**, with a focus on **relational plots**, which are used to visualize relationships between variables. Seaborn provides a high-level interface for creating **attractive, informative, and statistically meaningful visualizations** with minimal code.

---

## 🔹 What is Seaborn?

Seaborn is a Python data visualization library built on top of **Matplotlib**.  
It is mainly used for:
- Exploratory Data Analysis (EDA)  
- Statistical visualization  
- Relationship analysis between variables  

Seaborn works seamlessly with **Pandas DataFrames** and provides better default aesthetics than Matplotlib.

---

## 🔹 What Are Relational Plots?

Relational plots are used to **understand relationships between two or more variables**.

Seaborn provides two main relational plots:
- **Scatter Plot** → relationship between two numeric variables  
- **Line Plot** → trend or relationship over ordered data  

These plots help in:
- Identifying patterns  
- Understanding trends  
- Analyzing correlations  

---

## 🔹 Loading Sample Datasets Using Seaborn  

Seaborn provides built-in datasets for practice and learning.

```python
import seaborn as sns

df = sns.load_dataset("tips")
```

Useful for:
- Learning visualization techniques  
- Practicing EDA without external data  

---

## 🔹 Scatter Plot (`scatterplot()`)

Used to visualize the relationship between two numerical variables.

```python
sns.scatterplot(x="total_bill", y="tip", data=df)
```

Common use cases:
- Detecting correlation  
- Identifying clusters or patterns  
- Outlier detection  

---

## 🔹 Line Plot (`lineplot()`)

Used to show trends over time or ordered values.

```python
sns.lineplot(x="size", y="total_bill", data=df)
```

Common use cases:
- Trend analysis  
- Time-series visualization  
- Performance tracking  

---

## 🔹 Styling & Color Palettes  

Seaborn provides built-in styles and color palettes to enhance visual appearance.

### Setting Style
```python
sns.set_style("whitegrid")
```

### Using Color Palettes
```python
sns.color_palette("deep")
sns.color_palette("muted")
sns.color_palette("pastel")
```

Benefits:
- Better readability  
- Professional-looking plots  
- Consistent visual themes  

---

## 🧠 Key Learnings (Day 1 – Seaborn)

- Understood what Seaborn is and why it is used  
- Learned the concept of relational plots  
- Loaded built-in datasets using Seaborn  
- Created scatter plots using `scatterplot()`  
- Created line plots using `lineplot()`  
- Applied styles and color palettes for better visuals  

---

## 🎯 Outcome  

Day 1 built a strong foundation in **Seaborn and relational plotting**, preparing me for:
- Advanced EDA  
- Multivariate visualizations  
- Statistical plots  
- Data storytelling using visuals  

---

✅ **Day 1 of Seaborn Completed Successfully 🚀**  

