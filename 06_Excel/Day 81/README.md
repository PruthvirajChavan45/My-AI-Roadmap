# 📘 Excel – Phase 6 | Day 6  

## 📌 Topic: Lookup Functions in Excel  

On Day 6, I learned **Lookup functions**, which are among the most important and powerful features in Excel. Lookup functions are used to **search values in tables and return related information**, making them essential for data analysis, reporting, and automation.

---

## 🔹 VLOOKUP  

`VLOOKUP` searches for a value in the **first column of a table** and returns a corresponding value from another column.

**Syntax:**
```
=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])
```

**Example:**
```
=VLOOKUP(A2, A2:D10, 3, FALSE)
```

Limitations:
- Works only left to right  
- Column index is fixed  
- Breaks if columns are inserted  

---

## 🔹 HLOOKUP  

`HLOOKUP` searches for a value in the **first row of a table**.

**Syntax:**
```
=HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])
```

Used when data is arranged horizontally.

---

## 🔹 INDEX + MATCH  

A powerful and flexible alternative to VLOOKUP.

**INDEX**
```
=INDEX(array, row_num, [column_num])
```

**MATCH**
```
=MATCH(lookup_value, lookup_array, 0)
```

**Combined Example:**
```
=INDEX(B2:D10, MATCH(A2, A2:A10, 0), 2)
```

Advantages:
- Works left and right  
- Does not break when columns move  
- More flexible and reliable  

---

## 🔹 XLOOKUP  

`XLOOKUP` is the modern replacement for VLOOKUP and HLOOKUP.

**Syntax:**
```
=XLOOKUP(lookup_value, lookup_array, return_array)
```

Advantages:
- Works in any direction  
- No column index number needed  
- Built-in error handling  
- Cleaner and easier to use  

---

## 🔹 XMATCH  

`XMATCH` returns the **position of a lookup value**.

**Syntax:**
```
=XMATCH(lookup_value, lookup_array)
```

Used when:
- Finding position instead of value  
- Combined with INDEX for advanced lookups  

---

## 🧠 Key Learnings (Day 6 – Excel)

- Used VLOOKUP for vertical searches  
- Used HLOOKUP for horizontal tables  
- Applied INDEX + MATCH for flexible lookups  
- Learned modern lookup using XLOOKUP  
- Used XMATCH for position-based searching  
- Understood limitations of traditional lookup functions  

---

## 🎯 Outcome  

Day 6 strengthened my ability to:
- Retrieve data dynamically  
- Build automated reports  
- Replace manual searching  
- Use modern Excel lookup techniques efficiently  

---

✅ **Phase 6 – Excel Day 6 Completed Successfully 🚀**
