# 📊 Statistics – Day 45  

## 📌 Topic: Probability Rules  

---

## 📍 Addition Rule of Probability  
The addition rule is used to find the probability that **either event A or event B (or both)** will occur.

General rule:
```
P(A ∪ B) = P(A) + P(B) − P(A ∩ B)
```

We subtract the intersection part to avoid **double counting** when events overlap.

---

## 📍 Special Case: Mutually Exclusive Events  
If two events cannot occur at the same time, they are mutually exclusive.

In this case:
```
P(A ∩ B) = 0
P(A ∪ B) = P(A) + P(B)
```

Example: Getting a King or a Queen from a deck of cards.

---

## 📍 Multiplication Rule of Probability  
The multiplication rule is used to find the probability that **two events occur together**.

General rule:
```
P(A ∩ B) = P(A) × P(B | A)
```

This rule is applied when the outcome of the first event **affects** the second event.

---

## 📍 Special Case: Independent Events  
If two events do not affect each other, they are independent.

For independent events:
```
P(A ∩ B) = P(A) × P(B)
```

Example: Tossing a coin and spinning a spinner.

---

## 📍 Conditional Probability  
Conditional probability is the probability that **event B occurs given that event A has already occurred**.

Formula:
```
P(B | A) = P(A ∩ B) / P(A)
```

It is useful when dealing with **dependent events** and contingency tables.

---

