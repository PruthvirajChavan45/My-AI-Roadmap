
# 📊 Statistics – Day 49

## 📌 Topic: T-Test (Hypothesis Testing)

The **T-Test** is a statistical hypothesis test used to compare means when the **sample size is small (n < 30)** or when the **population standard deviation (σ) is unknown**. It helps decide whether the observed difference is statistically significant or due to random chance.

---

## 📍 When to Use T-Test
- Sample size is small (n < 30)
- Population standard deviation is unknown
- Data is approximately normally distributed

---

## 📍 One-Sample T-Test
Used to compare a **sample mean** with a **claimed population mean**.

### Formula:
t = ( x̄ − μ₀ ) / ( s / √n )

Where:
- x̄ = sample mean  
- μ₀ = claimed population mean  
- s = sample standard deviation  
- n = sample size  

### Degree of Freedom:
df = n − 1

---

## 📍 Decision Rule (Critical Value Method)
- Find **t-calculated**
- Find **t-critical** from t-table using df and significance level (α)
- If |t-calculated| > t-critical → Reject H₀
- Else → Fail to reject H₀

---

## 📍 Two-Sample T-Test
Used to compare means of **two independent samples**.

### Formula:
t = ( x̄₁ − x̄₂ ) / √( s₁²/n₁ + s₂²/n₂ )

Where:
- x̄₁, x̄₂ = sample means  
- s₁, s₂ = sample standard deviations  
- n₁, n₂ = sample sizes  

### Degree of Freedom:
df = min(n₁ − 1, n₂ − 1)

---

## 📍 One-Tailed vs Two-Tailed T-Test
- **One-Tailed Test**: Used when testing for a specific direction (greater or less)
- **Two-Tailed Test**: Used when testing for any difference

---

## 📍 Hypotheses Structure
- Null Hypothesis (H₀): No difference / claim is true
- Alternative Hypothesis (H₁): There is a difference / claim is false

---

## 📍 Key Notes
- If population standard deviation is known → use **Z-Test**
- If population standard deviation is unknown → use **T-Test**
- Even if n > 30, use T-Test when σ is unknown

---

## 📍 Conclusion Logic
- If test statistic lies in rejection region → Reject H₀
- Otherwise → Do not reject H₀

---

📌 This day focused on understanding **T-Test formulas, conditions, types, degrees of freedom, and decision rules** used in hypothesis testing.
