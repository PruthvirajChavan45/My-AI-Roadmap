
# 📘 NumPy – Day 5  

## 📌 Topic: Applying NumPy Concepts Through a Mini Project  

On Day 5, I focused on applying NumPy concepts in a **real-world mini project** to strengthen my understanding of array manipulation, logical operations, and problem-solving using Python.

Instead of only practicing theory, I implemented these concepts in a **Tic Tac Toe game project**, where NumPy plays a key role in handling game logic.

---

## 🔗 Project Link  

👉 **Tic Tac Toe Using NumPy (GitHub Repository):**  
https://github.com/PruthvirajChavan45/TicTacToe-Using-NumPy.git  

---

## 🧠 NumPy Concepts Applied in This Project  

### ✅ Array Representation
- Game board stored as a **3×3 NumPy array**
- Numerical representation used for faster computation

```
1   → Player X  
-1  → Player O  
0   → Empty cell
```

---

### ✅ Conditional Selection  
Used to:
- Check empty cells  
- Detect draw condition  
- Control valid moves  

Example logic:
```python
(board == 0).any()
```

---

### ✅ Advanced Indexing  
Used for:
- Row-wise checks  
- Column-wise checks  
- Diagonal extraction  

```python
board[i, :]
board[:, i]
np.trace(board)
np.trace(np.fliplr(board))
```

---

### ✅ Aggregation & Logical Operations  
Used NumPy aggregation to detect winners:

```python
abs(np.sum(row)) == 3
```

This allows efficient checking without loops.

---

## 🎮 Project Overview  

### Features:
- Interactive Tic Tac Toe game  
- Two-player mode (❌ vs ⭕)  
- Automatic win & draw detection  
- Restart functionality  
- Clean and responsive UI  
- NumPy-based game logic  

---

## 🛠 Tools & Technologies Used  

- **Python**
- **NumPy**
- **Streamlit**
- HTML & CSS (for UI styling)

---

## 📂 Project Structure  

```
TicTacToe-Using-NumPy/
│
├── app.py
├── Project UI.jpg
└── README.md
```

---

## 🎯 Learning Outcomes (Day 5)

By completing this day, I learned how to:

- Apply NumPy in real-world mini projects  
- Use array-based logic instead of loops  
- Implement conditional selection practically  
- Work with 2D arrays effectively  
- Combine logic + UI in a Python application  
- Write clean and recruiter-friendly documentation  

---

## 💡 Why This Matters for Data Roles

This project demonstrates:
- Strong understanding of NumPy fundamentals  
- Logical thinking & problem-solving  
- Ability to convert theory into working applications  
- Clean project structuring  
- Hands-on learning mindset  

---
