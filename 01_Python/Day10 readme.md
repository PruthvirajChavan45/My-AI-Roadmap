# Day 10 – Rock, Paper, Scissors (Mini Project [Link](https://github.com/PruthvirajChavan45/rock-paper-scissors-cli.git))

Today I built a Python CLI-based Rock–Paper–Scissors game.  
This project helped me practice user input handling, conditional logic, loops, and score tracking.

## 🔥 What I Learned Today
- Using random.choice / randint for computer decisions  
- Building game logic with if-elif conditions  
- Handling invalid inputs from users  
- Designing a clean CLI interface  
- Tracking scores until the player or computer reaches 5 points  
- Structuring a small project with clear outputs  

## 🧠 Project Overview
- User selects: 1 = Rock, 2 = Paper, 3 = Scissors  
- Computer randomly selects a move  
- Game compares both moves and decides the winner  
- First to **5 points** wins the match  
- Displays clear and friendly results for each round  

## 📝 Source Code


```python
import random 

cscore = 0      # Computer Score
hscore = 0      # Human Score

while True:

    print("\n-----------------------------------------------------------")
    print(f"Current Scores -> You: {hscore} | Computer: {cscore}\n")
    user = input("1 = Rock, 2 = Paper, 3 = Scissors. Choose: ")

    # Check if input is a number
    if not user.isdigit(): 
        print("Invalid input! Please enter a number only.\n")
        continue

    user = int(user)

    # Validate input range
    if user < 1 or user > 3: 
        print("⚠ Please enter a number **between 1 and 3 only.**\n")
        continue
    
    com = random.randint(1,3)

    # Display moves
    moves = ["Rock", "Paper", "Scissors"]

    # This list stores the names of moves.
    # User enters 1,2,3 but Python list indexes start at 0.
    # So (user - 1) gives the correct move name from the list.

    print(f"You chose: {moves[user-1]}")            
    print(f"Computer chose: {moves[com-1]}")

    # -----------------------
    # 🔥 RPS Logic 
    # -----------------------

    if user == com:
        print("🤝 It's a draw!\n")

    elif (user == 1 and com == 3) or \
         (user == 2 and com == 1) or \
         (user == 3 and com == 2):
        hscore += 1
        print("🎉 You won this round!\n")

    else:
        cscore += 1
        print("🤖 Computer won this round!\n")
    

    # -----------------------
    # 🔥 Win condition  
    # -----------------------
    if cscore == 5:
        print("\n-----------------------------------------------------------")
        print("👿 Computer won this game!")
        print("-----------------------------------------------------------\n")
        break
    elif hscore == 5:
        print("\n-----------------------------------------------------------")
        print("🏅 Congratulations! You won the game!")
        print("-----------------------------------------------------------\n")
        break
```

## 📌 Summary
This is my second full mini-project after the Number Guessing Game.  
It helped me improve logic-building skills and write cleaner Python code.
