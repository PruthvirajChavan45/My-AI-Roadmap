# 📊 Statistics – Day 38  

## 📌 Topic: Measures of Spread  

Measures of spread describe **how data is distributed or spread out** around the central value. While measures of central tendency tell us where the center is, measures of spread tell us **how far the values are from each other**.

---

## 📍 Range  
Range is the **difference between the maximum and minimum values** in a dataset.  
```
Range = Maximum value − Minimum value
```
It gives a quick idea of data spread but is highly affected by extreme values.

---

## 📍 Interquartile Range (IQR)  
Interquartile Range (IQR) measures the spread of the **middle 50% of the data**.  
```
IQR = Q3 − Q1
```
- Q1 (First Quartile): 25% of data below it  
- Q2 (Median): 50% of data below it  
- Q3 (Third Quartile): 75% of data below it  

IQR is not affected by outliers, so it is more reliable than range.

---

## 📍 Use Case of IQR  
- Used when data contains **outliers**  
- Helps identify **data clustering** and **data spread**  
- If **IQR is small and close to Q2**, data is clustered around the center  
- If **IQR is large and far from Q2**, data is more spread out  
- Commonly used in **box plots** and real-world datasets like salaries and income  

---

