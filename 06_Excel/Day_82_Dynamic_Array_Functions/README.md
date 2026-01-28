# 📘 Excel – Phase 6 | Day 7  

## 📌 Topic: Dynamic Array Functions  

On Day 7, I learned **Dynamic Array functions**, one of the most powerful modern features of Excel. These functions return multiple values automatically and spill results across cells, making formulas cleaner, faster, and more efficient.

---

## 🔹 What are Dynamic Arrays?

Dynamic arrays allow a single formula to return **multiple results** that automatically expand into neighboring cells (called *spill range*).

Benefits:
- No need to copy formulas  
- Automatic resizing  
- Cleaner and modern Excel formulas  

---

## 🔹 FILTER  

Used to extract data that meets specific conditions.

```
=FILTER(array, include)
```

Example:
```
=FILTER(A2:D20, D2:D20 > 80)
```

Used for:
- Conditional data extraction  
- Dynamic reporting  

---

## 🔹 SORT  

Used to sort data dynamically.

```
=SORT(array)
```

Example:
```
=SORT(A2:D20, 2, -1)
```

Sorts data in descending order.

---

## 🔹 UNIQUE  

Returns unique values from a list.

```
=UNIQUE(A2:A20)
```

Used for:
- Removing duplicates dynamically  
- Creating dropdown sources  

---

## 🔹 RANDARRAY  

Generates random numbers in array format.

```
=RANDARRAY(5, 3, 1, 100)
```

Used for:
- Sample data creation  
- Simulation and testing  

---

## 🔹 SEQUENCE  

Generates sequential numbers automatically.

```
=SEQUENCE(10)
```

Used for:
- Auto numbering  
- Date sequences  
- Index creation  

---

## 🔹 SORT + FILTER (Combined)

Dynamic arrays can be combined to create powerful formulas.

```
=SORT(FILTER(A2:D20, D2:D20 > 80), 2, -1)
```

Used to:
- Filter data based on conditions  
- Sort filtered results dynamically  

---

## 🧠 Key Learnings (Day 7 – Excel)

- Understood dynamic array behavior and spill ranges  
- Used FILTER for conditional extraction  
- Used SORT for dynamic sorting  
- Used UNIQUE for duplicate removal  
- Generated data using RANDARRAY  
- Created sequences using SEQUENCE  
- Combined SORT and FILTER for advanced analysis  

---

## 🎯 Outcome  

Day 7 strengthened my ability to:
- Build dynamic, formula-driven reports  
- Reduce manual formula copying  
- Create modern Excel solutions  
- Work efficiently with large datasets  

---

✅ **Phase 6 – Excel Day 7 Completed Successfully 🚀**

