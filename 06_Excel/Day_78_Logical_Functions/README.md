# 📘 Excel – Phase 6 | Day 3  

## 📌 Topic: Logical Functions in Excel  

On Day 3, I learned **Logical Functions**, which are used to apply conditions and decision-making logic in Excel. These functions are widely used in real-world reporting, analysis, and automation tasks.

---

## 🔹 IF Function  

The `IF` function evaluates a condition and returns different results based on TRUE or FALSE.

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
- Status assignment  
- Conditional labeling  

---

## 🔹 Nested IF  

Nested IF is used when **multiple conditions** need to be checked using IF inside another IF.

**Example:**
```
=IF(A1 >= 90, "A",
   IF(A1 >= 75, "B",
      IF(A1 >= 60, "C", "Fail")))
```

Used when:
- Multiple decision levels are required  
- Grading systems  
- Performance categorization  

⚠️ Can become complex if overused.

---

## 🔹 AND Function  

The `AND` function returns TRUE only when **all conditions are true**.

**Example:**
```
=AND(A1 >= 40, B1 >= 75)
```

---

## 🔹 OR Function  

The `OR` function returns TRUE when **any one condition is true**.

**Example:**
```
=OR(A1 >= 90, B1 = "Yes")
```

---

## 🔹 IF with AND / OR  

```text
=IF(AND(A1 >= 40, B1 >= 75), "Pass", "Fail")
```

```text
=IF(OR(A1 >= 90, B1 = "Yes"), "Eligible", "Not Eligible")
```

Used for advanced decision-making rules.

---

## 🔹 IFS Function  

The `IFS` function is an alternative to nested IF, making formulas cleaner and more readable.

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

---

## 🔹 SWITCH Function  

The `SWITCH` function checks one value against multiple exact matches.

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

Best used when values are fixed and predefined.

---

## 🧠 Key Learnings (Day 3 – Excel)

- Applied IF for basic decision-making  
- Used Nested IF for multiple conditions  
- Combined IF with AND / OR  
- Simplified logic using IFS  
- Used SWITCH for exact value matching  
- Built structured and dynamic Excel formulas  

---

## 🎯 Outcome  

Day 3 strengthened my understanding of **logical reasoning in Excel**, enabling me to:
- Automate decisions  
- Build smart spreadsheets  
- Create rule-based reports  
- Improve formula clarity  

---

✅ **Phase 6 – Excel Day 3 Completed Successfully 🚀**
