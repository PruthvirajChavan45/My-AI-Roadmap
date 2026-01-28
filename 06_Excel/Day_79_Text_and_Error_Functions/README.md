# 📘 Excel – Phase 6 | Day 4  

## 📌 Topic: Error Handling & Text Functions  

On Day 4, I learned two very important areas of Excel used in real-world data cleaning and reporting:  
**Error Handling** and **Text Functions**. These functions help manage formula errors and clean, transform, and manipulate text data efficiently.

---

## 🔹 1) Error Handling Functions  

Error handling functions prevent Excel formulas from showing errors like `#N/A`, `#DIV/0!`, `#VALUE!`, etc.

---

### ✅ IFNA  

Handles only `#N/A` errors.

**Syntax:**
```
=IFNA(value, value_if_na)
```

**Example:**
```
=IFNA(VLOOKUP(A1, B:C, 2, 0), "Not Found")
```

Used when working with lookup functions.

---

### ✅ IFERROR  

Handles **all types of Excel errors**.

**Syntax:**
```
=IFERROR(value, value_if_error)
```

**Example:**
```
=IFERROR(A1/B1, 0)
```

Used to make formulas clean and user-friendly.

---

## 🔹 2) Text Functions  

Text functions are used to clean, format, and extract information from text data.

---

### 🔸 LEFT, RIGHT, MID  

Used to extract text.

```
=LEFT(A1, 4)      → extract from start  
=RIGHT(A1, 2)     → extract from end  
=MID(A1, 2, 3)    → extract from middle  
```

---

### 🔸 TRIM & LEN  

```
=TRIM(A1)   → removes extra spaces  
=LEN(A1)    → counts characters  
```

Used for cleaning imported data.

---

### 🔸 UPPER, LOWER, PROPER  

```
=UPPER(A1)   → converts to uppercase  
=LOWER(A1)   → converts to lowercase  
=PROPER(A1)  → capitalizes first letters  
```

---

### 🔸 TRIM + PROPER (Combined)

```text
=PROPER(TRIM(A1))
```

Used to clean names and text formatting together.

---

### 🔸 SEARCH & FIND  

Used to locate text position.

```
=SEARCH("a", A1)  → not case-sensitive  
=FIND("A", A1)    → case-sensitive  
```

Returns the position number.

---

### 🔸 LEFT with SEARCH Combination  

Used to extract text before a specific character.

```text
=LEFT(A1, SEARCH("-", A1)-1)
```

Very common in real-world text cleaning.

---

### 🔸 SUBSTITUTE & REPLACE  

```
=SUBSTITUTE(A1, "old", "new")
=REPLACE(A1, 2, 3, "new")
```

- SUBSTITUTE → replaces text  
- REPLACE → replaces by position  

---

### 🔸 CONCAT, & , TEXTJOIN  

Used to combine text.

```
=CONCAT(A1, B1)
=A1 & " " & B1
=TEXTJOIN(" ", TRUE, A1, B1, C1)
```

TEXTJOIN is best for combining multiple values with a delimiter.

---

## 🧠 Key Learnings (Day 4 – Excel)

- Handled formula errors using IFNA and IFERROR  
- Extracted text using LEFT, RIGHT, MID  
- Cleaned text using TRIM and LEN  
- Formatted text using UPPER, LOWER, PROPER  
- Combined TRIM and PROPER for data cleaning  
- Located text using SEARCH and FIND  
- Extracted partial text using LEFT + SEARCH  
- Replaced text using SUBSTITUTE and REPLACE  
- Combined text using CONCAT, &, and TEXTJOIN  

---

## 🎯 Outcome  

Day 4 strengthened my ability to:
- Clean messy text data  
- Prevent formula errors  
- Prepare data for analysis  
- Build professional Excel reports  

---

✅ **Phase 6 – Excel Day 4 Completed Successfully 🚀**

