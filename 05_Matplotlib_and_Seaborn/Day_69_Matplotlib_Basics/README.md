# 📘 Matplotlib – Day 1  

## 📌 Topic: Introduction to Data Visualization with Matplotlib  

Today was my **first day of data visualization**, where I learned the fundamentals of **Matplotlib**, a powerful Python library used to create static, animated, and interactive visualizations. This session focused on understanding how data can be visually represented to gain insights more effectively than raw numbers.

---

## 🔹 What is Matplotlib?

Matplotlib is a **core visualization library in Python**, widely used in:
- Data analysis  
- Exploratory Data Analysis (EDA)  
- Machine learning workflows  
- Reporting and presentations  

It works seamlessly with **NumPy** and **Pandas**.

---

## 🔹 Basic Plotting Workflow  

Learned the standard steps to create a plot:

```python
import matplotlib.pyplot as plt
```

1. Prepare data (usually using NumPy or Pandas)  
2. Create a plot  
3. Customize labels and title  
4. Display the plot  

---

## 🔹 Line Plot  

Used to show trends or relationships between variables.

```python
plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot Example")
plt.show()
```

Used for:
- Trend analysis  
- Time series visualization  

---

## 🔹 Scatter Plot  

Used to visualize relationships between two numeric variables.

```python
plt.scatter(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot Example")
plt.show()
```

Helpful for:
- Pattern detection  
- Correlation analysis  

---

## 🔹 Bar Chart  

Used to compare values across categories.

```python
plt.bar(categories, values)
plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Bar Chart Example")
plt.show()
```

Commonly used in:
- Categorical comparisons  
- Summary reports  

---

## 🔹 Customizing Plots  

Learned basic customization options:
- Labels (`xlabel`, `ylabel`)  
- Titles (`title`)  
- Figure size (`figure(figsize=...)`)  
- Grid (`grid(True)`)  

These improve **readability and presentation quality**.

---

## 🔹 Understanding Axes & Figures  

- **Figure** → overall window or canvas  
- **Axes** → actual plotting area  

Understanding this concept helps in creating more complex plots later.

---

## 🧠 Key Learnings (Day 1 – Matplotlib)

- Introduction to data visualization  
- Importance of visualizing data  
- Created line, scatter, and bar plots  
- Understood plotting workflow  
- Customized plots for clarity  
- Connected NumPy data with Matplotlib visuals  

---

## 🎯 Outcome  

Day 1 built a **strong foundation in data visualization**, preparing me for:
- Exploratory Data Analysis (EDA)  
- Advanced plots (histogram, boxplot, subplots)  
- Real-world data storytelling  

---

✅ **Day 1 of Matplotlib Completed Successfully 🚀**  
*Next: Histograms, box plots, subplots, and advanced customization.*

