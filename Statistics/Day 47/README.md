# 📊 Statistics – Day 47  

## Hypothesis Testing
Hypothesis testing is a statistical decision-making framework used to test claims about a population using sample data.  
We start by assuming a default statement is true and then use evidence from data to decide whether to keep or reject it.

### Types of Hypothesis
- **Null Hypothesis (H₀):**  
  Represents “no effect”, “no difference”, or the current assumption.
- **Alternative Hypothesis (H₁):**  
  Represents a change, effect, or difference that challenges H₀.

The process always begins by assuming H₀ is true and then checking whether the data strongly contradicts it.

---

## Significance Level (α)
The significance level is the cut-off value used to decide whether to reject the null hypothesis.
- Common value: **α = 0.05**
- It represents the probability of making a wrong decision while rejecting H₀.
- α = 0.05 means we accept a 5% risk of being wrong.

---

## Type of Errors
When making decisions in hypothesis testing, two kinds of errors can occur:

- **Type I Error:**  
  Rejecting H₀ even though it is actually true (false alarm).
- **Type II Error:**  
  Failing to reject H₀ even though it is actually false (missed detection).

---

## One-Tailed and Two-Tailed Tests
- **One-Tailed Test:**  
  Used when we care about a change in only one direction (greater than or less than).
- **Two-Tailed Test:**  
  Used when we care about any difference, regardless of direction.

---

## P-Value
The p-value measures how extreme the observed data is assuming H₀ is true.
- Smaller p-value → stronger evidence against H₀.
- **Decision Rule:**
  - If `p-value < α` → Reject H₀
  - If `p-value ≥ α` → Fail to reject H₀

---

## Test Statistic
A test statistic is a numerical value calculated from sample data that helps decide whether to reject H₀.
It shows how far the sample result is from what we would expect if H₀ were true.

Common examples:
- Z-test  
- t-test  
- Chi-square test  
- F-test

