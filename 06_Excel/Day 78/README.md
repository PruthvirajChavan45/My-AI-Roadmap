# 📘 Excel – Phase 6 | Day 3  

## 📌 Topic: Logical Functions in Excel  

On Day 3, I learned **Logical Functions**, which are used to make decisions in Excel based on conditions. These functions are extremely important for data analysis, reporting, and business logic implementation.

---

## 🔹 IF Function  

The `IF` function checks a condition and returns different results based on whether the condition is TRUE or FALSE.

**Syntax:**
```
=IF(condition, value_if_true, value_if_false)
```

**Example:**
```
=IF(A1 >= 40, "Pass", "Fail")
```

Used for:
- Result calculation  
- Status identification  
- Conditional labeling  

---

## 🔹 AND Function  

The `AND` function checks multiple conditions and returns TRUE only if **all conditions are true**.

**Example:**
```
=AND(A1 >= 40, B1 >= 75)
```

Used when multiple rules must be satisfied.

---

## 🔹 OR Function  

The `OR` function returns TRUE if **any one condition is true**.

**Example:**
```
=OR(A1 >= 90, B1 = "Yes")
```

Used when at least one condition is enough.

---

## 🔹 Combining IF with AND / OR  

```text
=IF(AND(A1 >= 40, B1 >= 75), "Pass", "Fail")
```

```text
=IF(OR(A1 >= 90, B1 = "Yes"), "Eligible", "Not Eligible")
```

Used to apply complex business logic.

---

## 🔹 IFS Function  

The `IFS` function is used to test **multiple conditions without nested IFs**.

**Syntax:**
```
=IFS(condition1, result1, condition2, result2, ...)
```

**Example:**
```
=IFS(
A1 >= 90, "A",
A1 >= 75, "B",
A1 >= 60, "C",
A1 < 60, "Fail"
)
```

Makes formulas cleaner and easier to read.

---

## 🔹 SWITCH Function  

The `SWITCH` function compares one value against multiple options.

**Syntax:**
```
=SWITCH(expression, value1, result1, value2, result2, default)
```

**Example:**
```
=SWITCH(A1,
"Mon", "Monday",
"Tue", "Tuesday",
"Wed", "Wednesday",
"Invalid Day"
)
```

Best used when checking **exact matches**.

---

## 🧠 Key Learnings (Day 3 – Excel)

- Used IF for conditional decisions  
- Applied AND / OR for multiple conditions  
- Simplified logic using IFS  
- Used SWITCH for exact value matching  
- Built structured decision-based formulas  

---

## 🎯 Outcome  

Day 3 improved my ability to:
- Implement business rules in Excel  
- Create dynamic reports  
- Automate decision-making logic  
- Write clean and readable formulas  

---

✅ **Phase 6 – Excel Day 3 Completed Successfully 🚀**  

