# 📒 Data Visualization Revision – Matplotlib & Seaborn

## 📌 Introduction
This notebook is a complete revision of all data visualization concepts learned using Matplotlib and Seaborn. It covers basic, intermediate, and statistical plots commonly used in Exploratory Data Analysis (EDA). The goal of this notebook is to strengthen visualization fundamentals and build confidence in choosing the right plot for the right analysis.

---

## 🔷 Part 1: Matplotlib Revision

### 📍 What is Data Visualization?
Data visualization helps transform raw data into meaningful insights using graphical representation. It makes patterns, trends, and relationships easier to understand.

---

### 📍 Basic Line Plot
Used to show trends and continuous data.

```python
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Line Plot")
plt.show()
```

---

### 📍 Scatter Plot
Used to identify relationships and correlation between variables.

```python
plt.scatter(x, y)
```

---

### 📍 Bar Chart
Used to compare values across categories.

```python
plt.bar(categories, values)
```

---

### 📍 Plot Customization
- color  
- linestyle  
- linewidth  
- marker  
- grid  
- figsize  

Customization improves readability and presentation quality.

---

### 📍 Histogram
Used to understand data distribution.

```python
plt.hist(data)
```

---

## 🔷 Part 2: Seaborn Revision

### 📍 What is Seaborn?
Seaborn is a high-level visualization library built on Matplotlib that provides better default styling and direct support for Pandas DataFrames.

---

### 📍 Loading Dataset
```python
sns.load_dataset("tips")
```

---

## 🔹 Relational Plots

### Scatter Plot
```python
sns.scatterplot()
```

### Line Plot
```python
sns.lineplot()
```

Used to analyze relationships and trends between variables.

---

## 🔹 Categorical Plots

### barplot() vs countplot()
- barplot → shows aggregated values (mean by default)  
- countplot → shows frequency of categories  

---

### boxplot() & violinplot()
- boxplot → quartiles and outliers  
- violinplot → distribution shape and density  

---

### stripplot() & swarmplot()
- stripplot → raw data points (may overlap)  
- swarmplot → non-overlapping data points  

---

## 🔹 Distribution Plots

- histplot() → flexible histogram  
- kdeplot() → smooth density curve  
- rugplot() → raw observations  
- distplot() → deprecated (avoid usage)  
- hue → compare multiple distributions  

---

## 🔹 Regression & Mixed Plots

- regplot() → scatter with regression line  
- lmplot() → regression with categorical comparison  
- jointplot() → relationship + distribution  
- pairplot() → multi-variable relationship analysis  

---

## 🔹 Matrix / Grid Plots

### Heatmap
```python
sns.heatmap(df.corr())
```

Used for correlation and pattern detection.

### Clustermap
```python
sns.clustermap(df.corr())
```

Used to identify clustered relationships.

---

## 🔹 Styling & Themes

```python
sns.set_theme(style="whitegrid")
sns.color_palette("deep")
```

Styling improves visual clarity and professional presentation.

---

## 🧠 Key Takeaways

- Matplotlib is ideal for low-level plot control  
- Seaborn is best for statistical and EDA visualizations  
- Choosing the right plot is more important than styling  
- Visualization helps uncover patterns not visible in raw data  
- Clean plots lead to better data storytelling  

---

## 🎯 Conclusion
This notebook serves as a complete revision guide for Matplotlib and Seaborn. It consolidates all visualization concepts learned and prepares a strong foundation for advanced Exploratory Data Analysis and real-world data visualization tasks.

✅ Visualization revision completed successfully.

