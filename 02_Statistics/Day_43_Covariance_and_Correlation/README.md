
# 📊 Statistics – Day 43  

## 📌 Topic: Covariance & Correlation  

## 📌 Covariance  
Till now, we studied one variable at a time (like marks, height, weight).  
But when we want to understand **how two variables are related**, we use **covariance**.

Covariance tells us whether two variables:
- move **together**
- or move in **opposite directions**

### Formula:
```
Cov(X, Y) = Σ (Xi − X̄)(Yi − Ȳ) / n
```
Where:
- Xi , Yi → data values  
- X̄ , Ȳ → means of X and Y  
- n → number of observations  

### Types of Covariance:
- **Positive Covariance**  
  When one variable increases, the other also increases  
  (Example: hours studied ↑, marks ↑)

- **Negative Covariance**  
  When one variable increases, the other decreases  
  (Example: rank ↑, marks ↓)

Covariance only shows **direction of relationship**, not strength.

---

## 📌 Correlation  
Covariance can give very large or very small values, so it is hard to compare relationships.  
To solve this, we use **correlation**.

Correlation tells us:
- **how strong** the relationship is  
- **in which direction** the relationship exists  

Correlation is a **scaled version of covariance**.

### Formula:
```
r = Cov(X, Y) / (σX × σY)
```
Where:
- Cov(X, Y) → covariance of X and Y  
- σX → standard deviation of X  
- σY → standard deviation of Y  

### Range of Correlation:
- **+1** → perfect positive correlation  
- **−1** → perfect negative correlation  
- **0** → no correlation  

Correlation is always between **−1 and +1** and is widely used in data analysis and machine learning.

---
