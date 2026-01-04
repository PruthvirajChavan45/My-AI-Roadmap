# Day 9 – Number Guessing Game (Mini Project [Link](https://github.com/PruthvirajChavan45/number-guessing-cli.git))

Today I completed my mini-project: **Number Guessing CLI Game**.  
This is a Python command-line game where the user tries to guess a random number between 1 and 100.

---

## 🔗 Project Repository Link

Here is the full project with complete documentation and screenshots:

👉 **Number Guessing CLI Repo:**  
https://github.com/PruthvirajChavan45/number-guessing-cli

---

## 🎯 What I Learned Today

- How to use `random.randint()`
- Input validation using `.isdigit()`
- Range checking (1–100)
- While loops with conditions
- Hint logic (too high / too low)
- Clean CLI formatting
- Writing a professional README.md

---

## 🧠 Code Overview (Short Version)

```python
import random

num = random.randint(1, 100)
tries = 0

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Enter numbers only!")
        continue

    guess = int(guess)

    if guess == num:
        print("Correct! Attempts:", tries)
        break
    elif guess > num:
        print("Too high!")
    else:
        print("Too low!")

    tries += 1
