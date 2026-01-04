# 📊 Statistics – Day 50  

## 📌 Topic: Chi-Square Test & ANOVA Test  

---

## 🔹 Chi-Square Test  
The Chi-Square test is a **hypothesis testing method** used to check whether there is a **significant association between categorical variables** or whether observed frequencies differ from expected frequencies.

### 📍 Types of Chi-Square Test  
- Chi-Square Test of Independence  
- Chi-Square Goodness of Fit  

### 📍 Formula  
```
χ² = Σ (O − E)² / E
```
Where:  
- O = Observed frequency  
- E = Expected frequency  

### 📍 Expected Frequency  
```
E = (Row Total × Column Total) / Grand Total
```

### 📍 Degrees of Freedom  
```
df = (r − 1)(c − 1)
```
Where:  
- r = number of rows  
- c = number of columns  

### 📍 Hypotheses  
- Null Hypothesis (H₀): No association between variables  
- Alternative Hypothesis (H₁): There is an association between variables  

### 📍 Decision Rule  
- If χ² calculated > χ² critical → Reject H₀  
- Otherwise → Accept H₀  

### 📍 Use Cases  
- Gender vs Choice analysis  
- Survey data analysis  
- Market research  
- Categorical data testing  

---

## 🔹 ANOVA (Analysis of Variance)  
ANOVA is a statistical test used to determine whether there is a **significant difference between the means of two or more groups**.

### 📍 Purpose  
- Compare multiple group means at the same time  
- Avoid multiple t-tests  
- Identify whether at least one group mean is different  

### 📍 Types of ANOVA  
- One-Way ANOVA (one factor)  
- Two-Way ANOVA (two factors)  

### 📍 Hypotheses  
- Null Hypothesis (H₀): All group means are equal  
- Alternative Hypothesis (H₁): At least one group mean is different  

### 📍 Basic Concept  
ANOVA compares:  
- Variance **between groups**  
- Variance **within groups**  

### 📍 Decision Rule  
- If F-calculated > F-critical → Reject H₀  
- Otherwise → Accept H₀  

### 📍 Use Cases  
- Comparing student performance across classes  
- Testing effect of different treatments  
- Business and product comparison  
- Experimental data analysis  

---

