# 📘 Excel – Phase 6 | Day 5  

## 📌 Topic: Date & Time Functions  

On Day 5, I learned **Date and Time functions in Excel**, which are widely used in reporting, attendance tracking, payroll systems, project timelines, and business analysis. These functions help extract date components, calculate differences, and work efficiently with time-based data.

---

## 🔹 Extracting Day, Month & Year from a Date  

Used to extract specific parts from a full date.

```
=DAY(A1)     → returns day  
=MONTH(A1)   → returns month  
=YEAR(A1)    → returns year  
```

Helpful for:
- Monthly reports  
- Year-wise analysis  
- Date-based grouping  

---

## 🔹 TODAY() Function  

Returns the **current system date**.

```
=TODAY()
```

✔ Updates automatically every day  
✔ Used in dynamic reports  

---

## 🔹 NOW() Function  

Returns **current date and time**.

```
=NOW()
```

Includes:
- Date  
- Hours  
- Minutes  
- Seconds  

Used in time tracking and live dashboards.

---

## 🔹 WEEKNUM() Function  

Returns the **week number** of a given date.

```
=WEEKNUM(A1)
```

Used for:
- Weekly reports  
- Sales tracking  
- Work scheduling  

---

## 🔹 DATEDIF() Function  

Calculates the difference between two dates.

```
=DATEDIF(start_date, end_date, "d")   → days  
=DATEDIF(start_date, end_date, "m")   → months  
=DATEDIF(start_date, end_date, "y")   → years  
```

Commonly used for:
- Age calculation  
- Experience calculation  
- Duration tracking  

---

## 🔹 NETWORKDAYS() Function  

Calculates the number of **working days** between two dates (excluding weekends).

```
=NETWORKDAYS(start_date, end_date)
```

Used for:
- Project timelines  
- SLA calculation  
- Office working day tracking  

---

## 🔹 EOMONTH() Function  

Returns the **last date of a month**.

```
=EOMONTH(start_date, months)
```

Example:
```
=EOMONTH(A1, 0)
```

Returns month-end date of the given date.

Used in:
- Financial reporting  
- Monthly closing  
- Salary calculations  

---

## 🧠 Key Learnings (Day 5 – Excel)

- Extracted day, month, and year from dates  
- Used TODAY() for dynamic current date  
- Used NOW() for date with time  
- Calculated week numbers using WEEKNUM()  
- Found date differences using DATEDIF()  
- Calculated working days using NETWORKDAYS()  
- Identified month-end dates using EOMONTH()  

---

## 🎯 Outcome  

Day 5 strengthened my ability to:
- Perform date-based analysis  
- Build dynamic Excel reports  
- Calculate durations and timelines  
- Work efficiently with business calendars  

---

✅ **Phase 6 – Excel Day 5 Completed Successfully 🚀**

