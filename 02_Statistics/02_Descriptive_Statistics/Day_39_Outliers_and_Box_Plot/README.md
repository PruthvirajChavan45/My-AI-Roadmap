# 📊 Statistics – Day 39  

## 📌 Topic: Outliers & Box Plot  

---

## 📍 Outliers  
Outliers are **extreme values** in a dataset that are very different from most other observations.  
They can significantly affect measures like **mean and range**, so identifying them is important before analysis.

---

## 📍 Removing Outliers using Fences  
Outliers are detected using **Interquartile Range (IQR)**.

Formulas:
```
IQR = Q3 − Q1
Lower Fence = Q1 − 1.5 × IQR
Upper Fence = Q3 + 1.5 × IQR
```

- Any value **below the lower fence** or **above the upper fence** is considered an outlier.
- This method is reliable because it is not affected by extreme values.

---

## 📍 Five Number Summary  
The five-number summary describes a dataset using five key values:
1. Minimum  
2. First Quartile (Q1)  
3. Median (Q2)  
4. Third Quartile (Q3)  
5. Maximum  

It provides a clear picture of the data’s center, spread, and range.

---

## 📍 Box Plot  
A box plot is a graphical representation based on the **five-number summary**.

It consists of:
- A box from Q1 to Q3 (represents IQR)
- A line inside the box for the median (Q2)
- Whiskers extending to minimum and maximum values
- Points outside the whiskers represent outliers  

Box plots are useful for comparing distributions and detecting outliers quickly.

---

## 📍 Box Plot Example  
For a dataset:
```
Minimum = 10
Q1 = 20
Median = 30
Q3 = 40
Maximum = 60
```
- The box lies between 20 and 40  
- The median line is at 30  
- Any value outside the upper or lower fence is marked as an outlier  

Box plots are widely used in real-world data analysis such as salary distribution and exam scores.

---

