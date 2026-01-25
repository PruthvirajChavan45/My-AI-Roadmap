# 📘 Pandas – Day 7  

## 📌 Topics: Working with Time Series & Advanced Tricks (Performance)

On Day 7, I focused on **time series data handling** and **advanced Pandas techniques** that help write cleaner, more efficient, and better-performing data analysis code. These topics are commonly used in real-world analytics, reporting, and data engineering workflows.

---

## 📂 Folder Structure (As per Repository)

```
04_Pandas/
│
└── Day 66/
    ├── Advanced_Tricks_and_Performance.ipynb
    ├── README.md
    └── Working_with_Time_Series.ipynb
```

### 📁 Notebook Order
1. **Working_with_Time_Series.ipynb**  
2. **Advanced_Tricks_and_Performance.ipynb**  
3. **README.md**

---

## 🔹 Topic 1: Working with Time Series  

Time series data is data indexed by time (dates, timestamps). Pandas provides powerful tools to work with such data efficiently.

---

### 1️⃣ Converting Columns to Datetime (`pd.to_datetime`)  

Used to convert string or numeric columns into datetime format.

```python
df["date"] = pd.to_datetime(df["date"])
```

✔ Enables time-based operations  
✔ Required for resampling and time indexing  

---

### 2️⃣ Setting DateTime Index & Resampling  

After converting to datetime, the column can be set as an index.

```python
df = df.set_index("date")
```

#### Resampling Examples
```python
df.resample("D").sum()    # Daily
df.resample("W").mean()   # Weekly
df.resample("M").mean()   # Monthly
df.resample("Y").mean()   # Yearly
```

Used to:
- Aggregate data by time periods  
- Analyze trends and patterns  
- Compare performance over time  

---

### 🧪 Mini Project (Time Series Practice)

In this practice, I:
- Converted columns to datetime using `pd.to_datetime()`  
- Set a DateTime column as index  
- Resampled data to different time frequencies  

This helped reinforce practical time-series workflows.

---

## 🔹 Topic 2: Advanced Tricks & Performance  

Advanced methods help apply custom logic and transformations efficiently.

---

### 1️⃣ Applying Custom Functions with `apply()`  

`apply()` allows applying a custom function across rows or columns.

```python
df["Category"] = df["Score"].apply(lambda x: "High" if x >= 80 else "Low")
```

Used for:
- Custom calculations  
- Conditional transformations  
- Row-wise or column-wise logic  

---

### 2️⃣ Using `map()` for Element-wise Operations  

`map()` applies functions or mappings to a Pandas Series.

```python
df["City_Code"] = df["City"].map({"Delhi": 1, "Mumbai": 2})
```

✔ Faster for Series-level operations  
✔ Ideal for value mapping and transformations  

---

## 🧠 Key Learnings (Day 7)

- Converted data into datetime format  
- Set DateTime index for time-based analysis  
- Resampled data using daily, weekly, monthly, and yearly rules  
- Understood real-world time series aggregation  
- Applied custom logic using `apply()`  
- Used `map()` for efficient element-wise transformations  
- Improved performance-aware Pandas coding skills  

---

## 🎯 Outcome  

Day 7 strengthened my ability to:
- Work confidently with time-based datasets  
- Analyze trends over time  
- Apply advanced Pandas transformations  
- Write cleaner, more efficient data analysis code  

---

✅ **Day 7 of Pandas Completed Successfully 🚀**

