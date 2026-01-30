# 📘 Excel – Phase 6 | Day 10  

## 📌 Topic: Counting, Summation Functions & Tables  

On Day 10, I learned essential Excel functions used for **data analysis, reporting, and summarization**. These functions are widely used in real-world Excel tasks such as dashboards, MIS reports, and business analysis.

---

## 🔹 1) COUNT, SUM & SUBTOTAL Functions  

### ✅ COUNT Functions  

Used to count cells based on different conditions.

- **COUNT()** → counts only numeric values  
- **COUNTA()** → counts non-empty cells  
- **COUNTBLANK()** → counts empty cells  

Examples:
```
=COUNT(A1:A20)
=COUNTA(A1:A20)
=COUNTBLANK(A1:A20)
```

---

### ✅ Conditional Counting  

- **COUNTIF()** → single condition  
- **COUNTIFS()** → multiple conditions  

Examples:
```
=COUNTIF(A1:A20, ">50")
=COUNTIFS(A1:A20, ">50", B1:B20, "Delhi")
```

Used for:
- Condition-based analysis  
- Category-wise counting  

---

### ✅ SUM Functions  

- **SUM()** → total of numeric values  
- **SUMIF()** → sum based on one condition  
- **SUMIFS()** → sum based on multiple conditions  

Examples:
```
=SUM(A1:A20)
=SUMIF(A1:A20, ">50")
=SUMIFS(C1:C20, A1:A20, "Delhi", B1:B20, ">1000")
```

---

### ✅ SUBTOTAL() Function  

Used to calculate totals on filtered data.

```
=SUBTOTAL(function_num, range)
```

Key feature:
- Automatically ignores hidden rows  
- Works perfectly with filters  

Used for:
- Dynamic reports  
- Filter-based summaries  

---

## 🔹 2) Excel Tables  

Excel Tables convert a data range into a **structured and dynamic table**.

Features:
- Automatic formatting  
- Structured references  
- Auto-expanding ranges  
- Built-in filters and sorting  

Example:
```
Ctrl + T
```

Benefits:
- Cleaner data management  
- Reliable formulas  
- Better integration with PivotTables and charts  

---

## 🧠 Key Learnings (Day 10 – Excel)

- Used COUNT, COUNTA, COUNTBLANK effectively  
- Applied conditional counting with COUNTIF and COUNTIFS  
- Performed summation using SUM, SUMIF, SUMIFS  
- Used SUBTOTAL for filter-aware calculations  
- Created and managed Excel Tables  
- Worked with structured references  

---

## 🎯 Outcome  

Day 10 strengthened my ability to:
- Perform accurate data aggregation  
- Create dynamic reports  
- Analyze filtered datasets  
- Manage data efficiently using tables  

---

✅ **Phase 6 – Excel Day 10 Completed Successfully 🚀**

