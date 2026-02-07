# 📘 Excel – Phase 6 | Day 18  

## 📌 Topic: Time Intelligence, Relationship Functions & Power Pivot  

On Day 18, I explored **advanced DAX and Power Pivot concepts** focused on **time-based analysis, table relationships, and data modeling**. These topics are essential for building **professional dashboards, reports, and Business Intelligence (BI) solutions** in Excel.

This session helped me understand how Excel can work like a **mini Power BI tool**.

---

## 🔹 Time Intelligence Functions (DAX)

Time Intelligence functions are used to analyze **data over time** such as daily, monthly, quarterly, or yearly trends.

These functions help compare:
- Current vs previous period  
- Growth trends  
- Year-over-Year (YoY) performance  
- Month-over-Month (MoM) analysis  

### Functions Covered:
- `TOTALYTD()` → Year-to-Date total  
- `TOTALMTD()` → Month-to-Date total  
- `TOTALQTD()` → Quarter-to-Date total  
- `SAMEPERIODLASTYEAR()` → compare with last year  
- `DATEADD()` → shift dates forward/backward  

### Example:
```
Sales YTD = TOTALYTD(SUM(Sales[Amount]), Sales[Date])
```

```
Last Year Sales = CALCULATE(SUM(Sales[Amount]), SAMEPERIODLASTYEAR(Sales[Date]))
```

Used for:
- Sales dashboards  
- Performance tracking  
- Financial analysis  

---

## 🔹 Relationship Functions  

Relationship functions help manage **connections between multiple tables** in the Data Model.

They ensure correct data flow between related tables.

### Concepts Covered:
- Primary key & foreign key  
- One-to-Many relationships  
- Active & inactive relationships  
- Filter propagation  

### DAX Functions:
- `RELATED()` → fetch value from related table  
- `RELATEDTABLE()` → get related rows  

### Example:
```
Customer Name = RELATED(Customers[Name])
```

Used for:
- Combining data from multiple tables  
- Lookup operations  
- Relational analysis  

---

## 🔹 Power Pivot  

Power Pivot is used for:
- Handling large datasets (millions of rows)  
- Creating relationships between tables  
- Writing DAX formulas  
- Building advanced Pivot Tables  

Key Features:
- Data Model creation  
- Measures & calculated columns  
- Faster calculations  
- Professional reporting  

Used in:
- Business dashboards  
- Financial reports  
- Advanced analytics  

---

## 🧠 Key Learnings (Day 18 – Excel / DAX)

- Applied time intelligence functions for trend analysis  
- Compared performance across time periods  
- Built relationships between multiple tables  
- Used RELATED functions for cross-table calculations  
- Worked with Power Pivot for large-scale data modeling  
- Understood Excel’s BI capabilities  

---

## 🎯 Outcome  

Day 18 strengthened my ability to:
- Perform time-based business analysis  
- Create dynamic reports  
- Model relational datasets  
- Use Excel as a Business Intelligence tool  

---

✅ **Phase 6 – Excel Day 18 Completed Successfully 🚀**  

