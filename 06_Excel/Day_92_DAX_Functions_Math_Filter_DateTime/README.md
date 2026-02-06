# 📘 Excel – Phase 6 | Day 17  

## 📌 Topic: DAX Math, Filter & Date-Time Functions  

On Day 17, I continued learning **DAX (Data Analysis Expressions)** inside Power Pivot and explored **Mathematical, Filter, and Date-Time functions**. These functions help perform **advanced calculations, dynamic filtering, and time-based analysis** in the Excel Data Model.

This session focused on building more powerful and intelligent reports using DAX formulas.

---

## 🔹 DAX Math Functions  

Mathematical functions are used to perform **numeric calculations and aggregations**.

### Common Functions Covered:
- `SUM()` → total of values  
- `AVERAGE()` → mean value  
- `MIN()` → smallest value  
- `MAX()` → largest value  
- `COUNT()` → count numeric values  
- `DIVIDE()` → safe division (avoids divide-by-zero errors)  

### Example:
```
Total Sales = SUM(Sales[Amount])
Average Sales = AVERAGE(Sales[Amount])
Profit Margin = DIVIDE([Profit], [Sales])
```

Used for:
- KPIs  
- Totals and averages  
- Business metrics  

---

## 🔹 DAX Filter Functions  

Filter functions allow **conditional and context-based calculations**.

These are very powerful compared to normal Excel formulas.

### Common Functions Covered:
- `FILTER()` → filter rows based on condition  
- `CALCULATE()` → modify filter context  
- `ALL()` → remove filters  
- `COUNTROWS()` → count filtered rows  

### Examples:
```
High Sales = CALCULATE(SUM(Sales[Amount]), Sales[Amount] > 1000)
```

```
Filtered Data = FILTER(Sales, Sales[Region] = "West")
```

Used for:
- Conditional aggregations  
- Dynamic reports  
- Context-based analysis  

---

## 🔹 DAX Date-Time Functions  

Date-Time functions help analyze **time-based data** such as daily, monthly, or yearly performance.

### Functions Covered:
- `TODAY()` → current date  
- `NOW()` → current date & time  
- `YEAR()` → extract year  
- `MONTH()` → extract month  
- `DAY()` → extract day  
- `DATEDIFF()` → date difference  

### Example:
```
Year = YEAR(Sales[Date])
Days Gap = DATEDIFF(StartDate, EndDate, DAY)
```

Used for:
- Time intelligence  
- Sales trends  
- Monthly/Yearly reports  

---

## 🧠 Key Learnings (Day 17 – Excel / DAX)

- Performed aggregations using math functions  
- Applied conditional calculations using filter functions  
- Used CALCULATE for dynamic logic  
- Worked with date-time data in DAX  
- Built smarter and context-aware measures  
- Improved BI-style analysis skills  

---

## 🎯 Outcome  

Day 17 strengthened my ability to:
- Create advanced calculations  
- Build dynamic measures  
- Perform time-based analysis  
- Use DAX for professional reporting and dashboards  

---

✅ **Phase 6 – Excel Day 17 Completed Successfully 🚀**  

